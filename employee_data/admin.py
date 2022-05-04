from django.contrib import admin
from .models import Employees, Department

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['department','first_name', 'surname', 'emp_id', 'date_updated']
    # list_editable=['first_name', 'surname']

admin.site.register(Employees, EmployeeAdmin)
admin.site.register(Department)

