from django.db import models
from datetime import datetime

from authen.models import MyUser


class OrderManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)


class AudioManager(models.Manager):
    pass

class PublisherManager(models.Manager):
    def order_by_name(self):
        return self.get_queryset.order_by('name')


class Card(models.Model):
    number = models.PositiveIntegerField()
    due_date = models.DateField()
    cvv = models.SmallIntegerField()
    objects = models.Manager()


class Publisher(models.Model):
    title = models.CharField(max_length=255)


class TopRatedAuthorsManager(models.Manager):
    def get_queryset(self):
        return self.get_queryset.order_by('-rating')


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rating = models.FloatField()
    objects = models.Manager()
    topRated = TopRatedAuthorsManager()


class BookBase(models.Model):
    title = models.CharField(max_length=255, default='title')
    description = models.CharField(max_length=255, default="desc")
    release_date = models.DateTimeField(default=datetime.now)
    rating = models.IntegerField(default=5)  # set validator no more than 10
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='todo', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True


class NewBooksManager(models.Manager):
    def get_queryset(self):
        return self.get_queryset().order_by('-release_date')


# class BookReviewManager(models.Manager):
#     def get_queryset(self):
#         return self.objects.


class Book(BookBase):
    FORMAT_CHOICES = [
        ('HC', 'Hard Cover'),
        ('SC', 'Soft Cover'),
    ]
    num_pages = models.SmallIntegerField()
    format = models.CharField(max_length=2, choices=FORMAT_CHOICES)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    objects = models.Manager()
    new = NewBooksManager()
    # reviews = BookReviewManager()


class Genre(models.Model):
    name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    objects = models.Manager()


class Order(models.Model):
    status = models.BooleanField(default=True)
    items = models.CharField(max_length=255, default="item1")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    objects = OrderManager()


class Review(models.Model):
    review = models.TextField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    objects = models.Manager()


class AudioBook(BookBase):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    duration = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    objects = models.Manager()


class Categories(models.Model):
    name = models.CharField(max_length=255)
    audioBook = models.ForeignKey(AudioBook, on_delete=models.CASCADE)
    objects = models.Manager()
