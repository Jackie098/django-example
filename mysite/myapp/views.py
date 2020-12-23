from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'myapp/home.html')

def sum(request):
  return render(request, 'myapp/sum.html')

def toSum(request):
  x = int(request.POST['x'])
  y = int(request.POST['y'])

  context = {'result': x + y}

  return render(request, 'myapp/sum_result.html', context=context)