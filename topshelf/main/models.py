from django.db import models

# from authen.models import MyUser
# import authen


class Card(models.Model):
    number = models.PositiveIntegerField()
    due_date = models.DateField()
    cvv = models.SmallIntegerField()


class Publisher(models.Model):
    title = models.CharField(max_length=255)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Review(models.Model):
    review = models.TextField()
    user = models.ForeignKey('authen.MyUser', on_delete=models.CASCADE)


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    pass


class BookBase(models.Model):
    pass


class Book(BookBase):
    FORMAT_CHOICES = [
        ('HC', 'Hard Cover'),
        ('SC', 'Soft Cover'),
    ]
    num_pages = models.SmallIntegerField()
    format = models.CharField(max_length=2, choices=FORMAT_CHOICES)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
