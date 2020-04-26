from django.http import Http404
from rest_framework import status, mixins, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Book, AudioBook, Author
from main.serializers import BookSerializer, AudioBookSerializer, AuthorSerializer


class BookListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AuthorListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GenreListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoriesList(APIView):

    def get_object(self, pk):
        try:
            return AudioBook.objects.get(id=pk)
        except AudioBook.DoesNotExist as e:
            raise Http404


class AudioList(APIView):

    def get(self):
        audioLists = AudioBook.objects.all()
        serialiazer = AudioBookSerializer(audioLists,many=True)
        return Response(serialiazer.data,status = status.HTTP_200_OK)

    def post(self,request):
        serializer = AudioBookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_500_INTERNAL_SERVER_ERROR)


