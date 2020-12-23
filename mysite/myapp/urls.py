from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student_form/', views.student_form, name='student_form'),
    path('student/', views.student, name='student'),
    path('students/', views.students, name='students'),
]