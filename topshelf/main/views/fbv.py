from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from main.models import Genre, Book,Order
from rest_framework.decorators import api_view
from main.serializers import GenreSerializer, ReviewSerializer


@api_view(['GET', 'POST'])
def show_add_book_reviews(request, pk):
    try:
        books = Book.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"status": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)
    try:
        reviews = books.reviews.all()
    except ObjectDoesNotExist:
        return Response({"status": "Reviews of this Book does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(reviews)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error': 'bad request'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'DELETE'])
def get_delete_book_review(request, pk, pk2):
    try:
        books = Book.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"status": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)
    try:
        review = books.reviews.get(id=pk2)
    except ObjectDoesNotExist:
        return Response({"status": "Reviews of this Book does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response({"status": "Successfully deleted review"}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'bad request'}, status=status.HTTP_404_NOT_FOUND)



