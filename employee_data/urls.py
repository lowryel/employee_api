from django.urls import path
from .views import EmployeeAPIView, DetailAPIView


app_name='employee_data'
urlpatterns = [
    path('', EmployeeAPIView.as_view(), name='list'),
    # path('emp_detail/<int:pk>', employee_detail, name='detail'),
    path('emp_detail/<int:id>', DetailAPIView.as_view(), name='detail'),
]

