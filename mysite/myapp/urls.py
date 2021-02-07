from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('student/', views.student, name='student'),
    path('students/', views.students, name='students'),
    path('find_student/', views.find_student, name="find_student"),
    path('get_student/', views.read_student, name='get_student'),

    path('new_post_form/', views.new_post_form, name="new_post_form"),
    path('new_post_view/', views.new_post_view, name="new_post_view"),
]