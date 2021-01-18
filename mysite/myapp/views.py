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
  student1 = Student('111', 'Carlos', True)
  student2 = Student('222', 'Ruam', False)
  student3 = Student('333', 'Caki', False)

  students = [student1, student2, student3]
  context = {'students': students}

  return render(request, 'myapp/list_students.html', context=context)