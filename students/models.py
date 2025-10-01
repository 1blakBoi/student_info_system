from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    department = models.CharField(max_length=50)
    gpa = models.FloatField()
    image = models.ImageField(upload_to='uploads')
    #uploaded_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
