from cProfile import label
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Count

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

        
@receiver(post_save, sender=Employees)
def post_save_db_limit(sender, **kwargs):
    employee=Employees.objects.all().count()
    if employee>10:
        print(kwargs)
        print('you have been denied access. We have exceeded our limit')



