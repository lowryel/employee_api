from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from employee_data.models import Employees
from employee_data.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, authentication
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from .permissions import IsStaffEditorPermission

# Create your views here.

class EmployeeListCreateView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    queryset=Employees.objects.all()
    serializer_class=EmployeeSerializer
    # permission_class=[IsAdminUser]

    def create(self, serializer):
        serializer.save()



class EmployeeAPIView(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
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
    authentication_classes=[
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [IsStaffEditorPermission]
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
        return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee=self.get_objects(id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def request_data(request):
#     employee = Employees.objects.all()
#     if request.method=="GET":
#         serializer=EmployeeSerializer(employee, many=True)
 
#         return Response(serializer.data)


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
import requests
def apifunc(request):
    api_url = 'http://localhost:8000/emplist_create/'
    response=requests.get(api_url)
    res=response.json()
    for x in res:
        print(x['department'], x['first_name'], x['surname'])
    context={'api_url':res}
    print(res)
    return render(request, 'api.html', context)
