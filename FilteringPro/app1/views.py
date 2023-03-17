from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class EmpListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ('^eno',)
    ordering_fields= ('eno','esal')
    # def get_queryset(self):
    #     qs=Employee.objects.all()
    #     name=self.request.GET.get('ename')
    #     if name is not None:
    #         qs=qs.filter(ename__icontains=name)
    #     return qs
