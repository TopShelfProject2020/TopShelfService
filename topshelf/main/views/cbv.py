from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Book,AudioBook
from main.serializers import BookSerializer,AudioBookSerializer


class BookList(APIView):

    def get(self, request):
        bookLists = Book.objects.all()
        serializer = BookSerializer(bookLists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GenreList(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(id=pk)
        except Book.DoesNotExist as e:
            raise Http404


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


