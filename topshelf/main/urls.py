from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import viewsets
from main.views.cbv import BookListAPIView, GenreListApiView
from main.views.fbv import show_add_book_reviews

urlpatterns = [
    path('reviewList/', show_add_book_reviews),  # GET reviews

    path('bookList/', BookListAPIView.as_view()),  # GET POST book

    path('genreList/', GenreListApiView.as_view()),  # GET POST genre
]

router = DefaultRouter()
router.register(r'books', viewsets.BookViewSet, basename='books')
router.register(r'genres', viewsets.BookViewSet, basename='genres')


urlpatterns += router.urls
