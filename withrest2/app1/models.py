from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=64)
    sfees=models.FloatField()
    saddr=models.CharField(max_length=100)

