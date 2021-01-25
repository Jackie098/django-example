from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student_form/', views.student_form, name='student_form'),
    path('student/', views.student, name='student'),
    path('students/', views.students, name='students'),
    path('find_student/', views.find_student, name="find_student"),
    path('get_student/', views.read_student, name='get_student'),
]