from cProfile import label
from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=150, help_text="Enter your position here")

    def __str__(self):
        return self.name

class Employees(models.Model):
    department     =models.ForeignKey(Department, on_delete=models.PROTECT)
    first_name     =models.CharField(max_length=150)
    surname        =models.CharField(max_length=150)
    emp_id         =models.BigIntegerField()
    date_updated   =models.DateTimeField(auto_now_add=True)
    date_joined    =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
        
