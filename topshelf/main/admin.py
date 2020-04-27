from django.contrib import admin
from main.models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(AudioBook)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Order)