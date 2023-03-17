from rest_framework import serializers
from app1.models import Employee


def multiples_of_1000(value):
    if value % 1000 != 0:
        raise serializers.ValidationError('sal should be multiples of 1000')


class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=64)
    esal=serializers.FloatField(validators=[multiples_of_1000])
    eaddr=serializers.CharField(max_length=64)

    def validate_esal(self,value):
        if value<55555:
            raise serializers.ValidationError('emp sal should be minimum 55555')
        return value

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.esal = validated_data.get('esal', instance.esal)
        instance.eaddr = validated_data.get('eaddr', instance.eaddr)
        instance.save()
        return instance

    def validate(self,data):
        ename=data.get('ename')
        esal=data.get('esal')
        if ename=='sappy':
            if esal<300000:
                raise serializers.ValidationError('sappy sal should be min 3l')
        return data

