from main.models import AudioBook, Publisher, Genre, Book, Card,Order
from main.serializers import AudioBookSerializer, PublisherSerializer, GenreSerializer, BookSerializer,OrderSerializer

from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import IsAuthenticated

import logging
logger = logging.getLogger('api')


class AudioViewSet(viewsets.ModelViewSet,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated,)
    serializer_class = AudioBookSerializer

    def get_queryset(self):
        return AudioBook.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'Created Audio: {serializer.instance}')


    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Updated Audio: {serializer.instance}')


    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'Deleted Audio: {instance}')



class PublisherViewSet(viewsets.ModelViewSet,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated,)
    serializer_class = PublisherSerializer

    def get_queryset(self):
        return Publisher.objects.order_by_name()

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'Created Publisher: {serializer.instance}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Updated Publisher: {serializer.instance}')

    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'Deleted Publisher: {instance}')


class BookViewSet(viewsets.ModelViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class GenreViewSet(viewsets.ModelViewSet,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated,)
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class CardViewSet(viewsets.ModelViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated,)
    serializer_class = PublisherSerializer

    def get_queryset(self):
        return Card.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class OrderViewSet(viewsets.ModelViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'Created Order: {serializer.instance}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Updated Order: {serializer.instance}')

    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'Created Order: {instance}')
