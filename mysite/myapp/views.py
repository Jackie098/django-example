from django.shortcuts import render
from .models import Student


# Create your views here.
def home(request):
  return render(request, 'myapp/home.html')

def student_form(request):
  return render(request, 'myapp/student_form.html')

def student(request):
  registration = request.POST['registration']
  name = request.POST['name']
  scholarship = False

  if 'scholarship' in request.POST:
    scholarship = True

  student = Student(registration=registration, name=name, scholarship=scholarship)
  student.save()
  
  context = {'student': student}

  return render(request, 'myapp/student.html', context=context)

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