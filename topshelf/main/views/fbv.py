from rest_framework.response import Response
from rest_framework import status
from main.models import Genre
from rest_framework.decorators import api_view
from main.serializers import GenreSerializer


@api_view(['GET', 'POST'])
def show_genre_list(request):
    if request.method == 'GET':
        genre_list = Genre.objects.all()
        serializer = GenreSerializer(genre_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error': 'bad request'}, status=status.HTTP_404_NOT_FOUND)
