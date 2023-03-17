from django.shortcuts import render
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework import mixins
from rest_framework.generics import ListAPIView,RetrieveAPIView

# Create your views here.
class EmpListCreateModelMixin(mixins.CreateModelMixin,ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmpRUDModelMixin(mixins.UpdateModelMixin,mixins.DestroyModelMixin,RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

