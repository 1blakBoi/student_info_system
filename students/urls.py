from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('all-student/', views.all_students, name='all-students'),
    path('<int:id>', views.view_student, name='student'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student_info, name='edit-student'),
    path('delete/<int:id>/', views.delete_student_info, name='delete-student'),
    path('registration/', views.user_registration, name='user-registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)