from django.db import models

# Create your models here.

class Student:
  def __init__(self, registration=None, name=None, scholarship=False): #If it has no value, NONE is the default
    self.registration = registration
    self.name = name
    self.scholarship = scholarship

    def __str__(self):
      return 'registration={}, name={}, scholarship={}'.format(self.registration, self.name, self.scholarship)