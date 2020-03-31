from django.db import models
from main.models import Writer


class BookBase(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Writer, on_delete=models.CASCADE)


class Book(BookBase):
    description = models.TextField(max_length=800)
    date_added = models.DateField(auto_now_add=True)
    rating = models.FloatField(default=0.0)
    num_pages = models.IntegerField()
    reviews = models.ForeignKey(Review, )

