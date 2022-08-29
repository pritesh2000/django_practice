from rest_framework import serializers

from .models import Customer

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    city = serializers.IntegerField()
    roll = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=10)

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    serial_no = serializers.IntegerField()
    site = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)