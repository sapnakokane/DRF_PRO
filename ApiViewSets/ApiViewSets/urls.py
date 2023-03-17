"""ApiViewSets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.EmpApiView.as_view()),
    path('apic/',views.EmployeeCreateApiView.as_view()),
    path('apir/<id>',views.EmployeeRetrieveApiView.as_view()),
    path('apiu/<pk>',views.EmployeeUpdateApiView.as_view()),
    path('apid/<pk>',views.EmployeeDestroyApiView.as_view()),
    path('apilc/',views.EmployeeLCApiView.as_view()),
    path('apiru/<pk>',views.EmployeeRUApiView.as_view()),
    path('apird/<pk>',views.EmployeeRDApiView.as_view()),
    path('apirud/<pk>',views.EmployeeRUDApiView.as_view()),
    path('apilistc/',views.EmpListCreateAPIView.as_view()),
    path('apireadud/<pk>',views.EmpRetrieveUpdateDestroyAPIView.as_view()),
]
