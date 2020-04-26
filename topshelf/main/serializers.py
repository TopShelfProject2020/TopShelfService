from rest_framework import serializers
from main.models import *


class AudioBookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = AudioBook
        fields = ('__all__')


class PublisherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publisher
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ('__all__')


class CategoriesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Categories
        fields = ('__all__')


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        g = Genre(**validated_data)
        g.save()
        return g

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Review
        fields = ('__all__')


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = ('__all__')


class CardSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Card
        fields = ('__all__')


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    review = ReviewSerializer(many=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('__all__')

    def create(self, validated_data):
        reviews = validated_data.pop('review')
        book = Book.objects.create(**validated_data)
        for r in reviews:
            Review.objects.create(book=book, **r)
        return book
