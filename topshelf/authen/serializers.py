from rest_framework import serializers
from authen.models import *


class MyUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email', 'is_staff')

    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
