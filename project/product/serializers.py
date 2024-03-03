from rest_framework import serializers

from .models import Product, Lesson
from .permissions import StudentAccessToProduct


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'name',
            'link'
        ]


class ProductSerializer(serializers.ModelSerializer):
    # lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'name',
            'author',
            'start_datetime',
            'price',
            'lessons_amount',
            # 'lessons'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'name',
            'author',
            'start_datetime',
            'price',
            'lessons_amount',
            'lessons'
        ]