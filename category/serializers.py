# category/serializers.py
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'brand', 'brand_name', 'created_at')