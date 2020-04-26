from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny

from authen.models import MyUser
from authen.serializers import MyUserSerializer


class Register(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return MyUserSerializer
