from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Student, Post


# Create your views here.
def home(request):
  return render(request, 'myapp/home.html')

def student_form(request):
  return render(request, 'myapp/student_form.html')

def students(request):
  students = Student.objects.all()

  # students = [student1, student2, student3]
  context = {'students': students}

  return render(request, 'myapp/list_students.html', context=context)

def find_student(request):
  return render(request, 'myapp/student_find.html')

def read_student(request):
  id = request.POST['id']

  student = Student.objects.get(pk=id)

  print(student)
  return render(request, 'myapp/home.html')

@login_required
def new_post_form(request):
  return render(request, 'myapp/post_form.html')

@login_required
def new_post_view(request):
  if request.method != 'POST':
    print('The method isnt POST')

    return redirect('students')
  
  if not request.user.is_authenticated:
    print('User isnt authenticated')

    return redirect('login_form')
  
  post_text = request.POST['post_text']
  user = request.user
  student = Student.objects.get(user=user)

  post = Post(text=post_text, student=student)
  post.save()

  return redirect('home')

@login_required
def student_posts(request):
  user = request.user
  student = Student.objects.get(user=user)

  posts = student.post_set.all()

  context = {'posts': posts}

  return render(request, 'myapp/my_posts.html', context=context)