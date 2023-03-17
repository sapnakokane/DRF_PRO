from django.contrib import admin
from app1.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sno','sname','sfees','saddr']

admin.site.register(Student,StudentAdmin)