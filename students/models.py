from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    department = models.CharField(max_length=50)
    gpa = models.FloatField()


    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
