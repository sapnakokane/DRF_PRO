from django.shortcuts import render
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class EmployeeListApiView(APIView):
    def get(self,request,format=None):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(serializer.data)

# to get list of all resources ListAPIView class is best suitable
from rest_framework.generics import ListAPIView
class EmpApiView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get_queryset(self):
        qs = Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs

from rest_framework.generics import CreateAPIView
class EmployeeCreateApiView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from rest_framework.generics import RetrieveAPIView
class EmployeeRetrieveApiView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

from rest_framework.generics import UpdateAPIView
class EmployeeUpdateApiView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from rest_framework.generics import DestroyAPIView
class EmployeeDestroyApiView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from rest_framework.generics import ListCreateAPIView
class EmployeeLCApiView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from rest_framework.generics import RetrieveUpdateAPIView
class EmployeeRUApiView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from rest_framework.generics import RetrieveDestroyAPIView
class EmployeeRDApiView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView
class EmployeeRUDApiView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#implementing all curd operations by using only 2 end points
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
class EmpListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class EmpRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



