from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

class UpdateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["title", "description"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)