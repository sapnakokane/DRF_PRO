from rest_framework import serializers
from app1.models import Student

def multiples_of_10000(value):
    if value %10000 !=0:
        raise serializers.ValidationError('fees in multiples of 10000')

class StudentSerializer(serializers.ModelSerializer):
    sfees=serializers.FloatField(validators=[multiples_of_10000,])
    class Meta:
        model=Student
        fields='__all__'


