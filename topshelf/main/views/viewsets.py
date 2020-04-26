from main.models import AudioBook, Publisher, Genre, Book
from main.serializers import AudioBookSerializer, PublisherSerializer

from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import IsAuthenticated


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

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class PublisherViewSet(viewsets.ModelViewSet,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated,)
    serializer_class = PublisherSerializer

    def get_queryset(self):
        return Publisher.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class BookViewSet(viewsets.ModelViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated,)
    serializer_class = AudioBookSerializer

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
    serializer_class = PublisherSerializer

    def get_queryset(self):
        return Genre.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()