
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def index(request):
    students = Student.objects.all()
    student_count = students.count()
    context = {'students': students, 'student_count': student_count}
    return render(request, 'students/index.html', context)


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('homepage'))



def add_student(request):
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
            return render(request, 'students/add_student_form.html', {'form': StudentForm(), 'success': True})
    else:
        form = StudentForm()
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
        return HttpResponseRedirect(reverse('homepage'))

