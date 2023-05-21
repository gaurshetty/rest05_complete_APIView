from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        emps = Employee.objects.all()
        serialize = EmployeeSerializer(emps, many=True)
        return Response(serialize.data)
    def post(self, request, *args, **kwargs):
        serialize = EmployeeSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailAPIView(APIView):
    def get(self, request, id):
        try:
            emp = Employee.objects.get(id=id)
            serialize = EmployeeSerializer(emp)
            return Response(serialize.data)
        except Employee.DoesNotExist:
            return Response({'msg': 'Employee data does not exist'}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, id):
        emp = Employee.objects.get(id=id)
        serialize = EmployeeSerializer(emp, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        emp = Employee.objects.get(id=id)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
