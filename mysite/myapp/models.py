from django.db import models

# Create your models here.

class Student:
  def __init__(self, registration=None, name=None): #If it has no value, NONE is the default
    self.registration = registration
    self.name = name

    def __str__(self):
      return 'registration={}, name={}'.format(self.registration, self.name)