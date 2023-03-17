from django.shortcuts import render
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView
from app1.pagination import MyPagination,MyPagination2,MyPagination3


# Create your views here.
class EmpListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination3



