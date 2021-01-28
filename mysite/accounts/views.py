from django.shortcuts import render

# Create your views here.
def signup(request):
  return render(request, 'accounts/signup.html')

def register(request):
  print(request)
  return render(request, 'myapp/home.html')