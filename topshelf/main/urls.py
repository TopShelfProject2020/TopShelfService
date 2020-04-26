from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import viewsets
from main.views.cbv import BookListAPIView, GenreListApiView, AuthorListAPIView
from main.views.fbv import show_add_book_reviews

urlpatterns = [
    path('book/<int:pk>/review/', show_add_book_reviews),  # get or create review for book

    path('bookList/', BookListAPIView.as_view()),  # GET POST book

    path('authorList/', AuthorListAPIView.as_view()),  # GET author
    path('author/', AuthorListAPIView.as_view()),  # new author

    path('genreList/', GenreListApiView.as_view()),  # GET POST genre



]

router = DefaultRouter()
router.register(r'books', viewsets.BookViewSet, basename='books')
router.register(r'genres', viewsets.BookViewSet, basename='genres')
router.register(r'publisher', viewsets.PublisherViewSet, basename='publisher')


urlpatterns += router.urls
