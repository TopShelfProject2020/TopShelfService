from rest_framework import serializers
from authen.models import *


class MyUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email', 'is_staff')

