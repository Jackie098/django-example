from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from myapp.models import Student

# Create your views here.
def signup(request):
  return render(request, 'accounts/signup.html')

def register(request):
  # Check if it is POST method
  if request.method != 'POST':
    messages.error(request, 'Fill out all of the fields')

    return redirect('signup')

  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']
  password2 = request.POST['password2']
  registration = request.POST['registration']
  name = request.POST['name']
  scholarship = False

  if 'scholarship' in request.POST:
    scholarship = True

  # Check if the PASSWORD's are iquals
  if password != password2:
    messages.info(request, 'The passwords dont match')

    return redirect('signup')

  # Check if USERNAME already exists
  if User.objects.filter(username=username).exists():
    messages.error(request, 'The username already exists')

    return redirect('signup')

  # Check if EMAIL already exists
  if User.objects.filter(email=email).exists():
    messages.error(request, 'The email already exists')

    return redirect('signup')

  user = User.objects.create_user(username=username, email=email, password=password)
  user.save()

  # Now, save the student in database
  # Student inherits from user
  Student.objects.create(
    user = user,
    registration = registration,
    name = name,
    scholarship = scholarship,
  )

  print('usersaved = [username={}. email={}, password={}]'.format(username, email, password))  
    
  return render(request, 'myapp/home.html')

def login_form(request):
  return render(request, 'accounts/login.html')

def login_view(request):
  if request.method != 'POST':
    messages.error(request, 'Fill out all of the fields')

    return redirect('login_form')

  username = request.POST['username']
  password = request.POST['password']

  user = authenticate(username=username, password=password)

  if user is None:
    return redirect('login_form')
  
  login(request, user) # Login finally

  return redirect('home')

def logout_view(request):
  logout(request)

  return redirect('home')