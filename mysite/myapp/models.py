from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)

    registration = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    scholarship = models.BooleanField(default=False)

    def __str__(self):
      return 'registration={}, name={}, scholarship={}'.format(self.registration, self.name, self.scholarship)


class Post(models.Model):
  text = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True, null=False)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)

  def __str__(self):
    return "{}, ({}))".format(self.text, self.date)