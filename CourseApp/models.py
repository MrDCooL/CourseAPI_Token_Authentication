from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AppUser(AbstractUser):
    ROLE_CHOICES = [
        ("instructor","Instructor"),
        ("student","Student")
    ]

    role = models.CharField(max_length= 100 , choices=ROLE_CHOICES)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(AppUser,on_delete=models.CASCADE)

class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_on = models.DateField(auto_now_add=True)