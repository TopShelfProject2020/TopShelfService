from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authen.models import MyUser
from authen.serializers import MyUserSerializer

import logging
logger = logging.getLogger('api')


class Register(mixins.CreateModelMixin, GenericAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return MyUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info(f'User with id = {serializer.data["id"]} was created')
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)