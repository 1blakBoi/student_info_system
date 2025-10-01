
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, RegistrationForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'students/index.html')


def all_students(request):
    students = Student.objects.all()
    student_count = students.count()
    context = {'students': students, 'student_count': student_count}
    return render(request, 'students/all_student.html', context)


def user_registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/user_reg.html', context)

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('homepage'))

def add_student_info(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_department = form.cleaned_data['department']
            new_gpa = form.cleaned_data['gpa']
            new_image = form.cleaned_data['image']

            new_student = Student(
                student_id = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                department = new_department,
                gpa = new_gpa,
                image = new_image
                )
            
            new_student.save()
            if request.user.is_staff:
                return redirect('all-students')
            else:
                return redirect('dashboard')
        return render(request, 'students/add_student_form.html', {'form': StudentForm(), 'success': True})
    
    return render(request, 'students/add_student_form.html', {'form': form})

def edit_student_info(request, id):
    students = Student.objects.get(pk=id)
    form = StudentForm(instance=students)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=students)
        if form.is_valid():
            form.save()
            context = {'form': form, 'success': True}
            return render(request, 'students/edit_form.html', context)
    else:
        students = Student.objects.get(pk=id)
        form = StudentForm(instance=students)
        context = {'form': form}
    return render(request, 'students/edit_form.html', context)

def delete_student_info(request, id):
    if request.method == 'POST':
        students = Student.objects.get(pk=id)
        students.delete()
        return HttpResponseRedirect(reverse('all-students'))  

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('all-students')
            else:
                return redirect('dashboard')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('homepage')

@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    return render(request, 'students/students_dashboard.html', {'student': student})
