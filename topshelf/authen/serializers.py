from rest_framework import serializers
from authen.models import *
from main.serializers import OrderSerializer


class MyUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email', 'is_staff', 'orders')

