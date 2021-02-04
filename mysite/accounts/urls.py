from django.urls import path

from . import views

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('register/', views.register, name='register'),
  path('login_form/', views.login_form, name='login_form'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout')
]