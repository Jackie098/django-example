from django.db import models

# Create your models here.

class Student(models.Model):
  # def __init__(self, registration=None, name=None, scholarship=False): #If it has no value, NONE is the default
    registration = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    scholarship = models.BooleanField(default=False)

    def __str__(self):
      return 'registration={}, name={}, scholarship={}'.format(self.registration, self.name, self.scholarship)