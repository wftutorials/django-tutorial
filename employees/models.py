from django.db import models

# Create your models here.
class Employees(models.Model):
    firstname = models.CharField(max_length=125)
    lastname = models.CharField(max_length=125)
    department = models.CharField(max_length=50)
    employeeid = models.IntegerField()
    email = models.CharField(max_length=65)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Departments(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30)