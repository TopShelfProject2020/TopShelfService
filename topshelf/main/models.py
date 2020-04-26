from django.db import models
from datetime import datetime


class OrderManager(models.Manager):
    def for_user(self,user):
        return self.filter(user=user)


class AudioManager(models.Manager):
    pass


class Card(models.Model):
    number = models.PositiveIntegerField()
    due_date = models.DateField()
    cvv = models.SmallIntegerField()


class Publisher(models.Model):
    title = models.CharField(max_length=255)


class TopRatedAuthorsManager(models.Manager):
    def get_query_set(self):
        return self.get_queryset.order_by('-rating')


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rating = models.FloatField()
    objects = models.Manager
    topRated = TopRatedAuthorsManager()


class Review(models.Model):
    review = models.TextField()
    user = models.ForeignKey('authen.MyUser', on_delete=models.CASCADE)
    objects = models.Manager


class Genre(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager


class Order(models.Model):
    status = models.BooleanField(default=True)
    items = models.CharField(max_length=255,default="item1")
    user = models.ForeignKey('authen.MyUser', on_delete=models.CASCADE,default=1)

    objects = OrderManager()


class Categories(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager


class BookBase(models.Model):
    title = models.CharField(max_length=255,default='title')
    description = models.CharField(max_length=255,default="desc")
    release_date = models.DateTimeField(default=datetime.now())
    rating = models.IntegerField(default=5)
    price = models.IntegerField(default=100)
    image = models.CharField(max_length=255,default="image")
    reviews = models.ForeignKey(Review, on_delete = models.CASCADE)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    category = models.ManyToManyField(Categories)

    class Meta:
        abstract = True


class NewBooksManager(models.Manager):
    def get_query_set(self):
        return self.get_queryset().order_by('-release_date')


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


class AudioBook(BookBase):
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
    ]

    duration = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    objects = models.Manager()