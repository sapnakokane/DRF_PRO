from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.serializers import NameSerializer
from rest_framework.viewsets import ViewSet


# Create your views here.
class TestApiView(APIView):
    def get(self,request,*args,**kwargs):
        colors=['RED','Yellow','GREEN','Blue']
        return Response({'msg':'welcome to colourful world','colors':colors})

    def post(self,request,*args,**kwargs):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {}, happy colorful beautiful day'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)

    def put(self,request,*args,**kwargs):
        return Response({'msg':"this msg is from put method"})

    def patch(self,request,*args,**kwargs):
        return Response({'msg':"this msg is from patch method"})

    def delete(self,request,*args,**kwargs):
        return Response({'msg':"this msg is from delete method"})

class TestViewSet(ViewSet):
    def list(self,request):
        colors=['red','yellow','brown','burgendy']
        return Response({'msg':"colorful 2023",'colors':colors})

    def create(selfself,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} your life will b settled in 2023'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors)

    def retrieve(self,request,pk=None):
        return Response({'msg':"this is from retieve method"})

    def update(self,request,pk=None):
        return Response({'msg':"this is from update method"})

    def partial_update(self,request,pk=None):
        return Response({'msg':"this is from partial_update method"})

    def destroy(self,request,pk=None):
        return Response({'msg':"this is from destroy method"})


