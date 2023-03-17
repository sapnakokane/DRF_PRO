import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','PaginationPro.settings')
import django
django.setup()

from app1.models import Employee
from faker import *
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,20000)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
        print(emp_record)
populate(120)


