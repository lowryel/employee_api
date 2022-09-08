from .models import Employees
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=['department','first_name', 'surname', 'emp_id']
        


