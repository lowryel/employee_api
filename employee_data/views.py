from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from employee_data.models import Employees
from employee_data.serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class EmployeeAPIView(APIView):
    def get(self, request):
        employee=Employees.objects.all()
        emp_serializer=EmployeeSerializer(employee, many=True)
        return Response(emp_serializer.data)

    def post(self, request):
        emp_serializer=EmployeeSerializer(data=request.data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response(emp_serializer.data, status=status.HTTP_201_CREATED)
        return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailAPIView(APIView):

    def get_objects(self, id):
        try:
           return Employees.objects.get(id=id)
        except Employees.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        employee=self.get_objects(id)
        emp_serializer=EmployeeSerializer(employee)
        return Response(emp_serializer.data)

    def put(self, request, id): # To update an employee instance
        employee=self.get_objects(id)
        emp_serializer=EmployeeSerializer(employee, data=request.data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response(emp_serializer.data)
        return Response(emp_serializer, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee=self.get_objects(id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        



# @api_view(['GET', 'PUT', 'DELETE'])
# def employee_detail(request, pk):
#     try:
#         employee=Employees.objects.get(pk=pk)
#     except Employees.DoesNotExist:
#         return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

#     if request.method=='GET':
#         emp_serializer=EmployeeSerializer(employee)
#         return Response(emp_serializer.data)
#     elif request.method=='PUT':
#         emp_serializer=EmployeeSerializer(employee, data=request.data)
#         if emp_serializer.is_valid():
#             emp_serializer.save()
#             return Response(emp_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method=='DELETE':
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


