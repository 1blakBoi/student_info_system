from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('<int:id>', views.view_student, name='student'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student_info, name='edit-student'),
    path('delete/<int:id>/', views.delete_student_info, name='delete-student'),
]