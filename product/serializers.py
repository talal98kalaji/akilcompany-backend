# product/serializers.py
from rest_framework import serializers
from .models import Product, ProductVariant
import json 

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ('id', 'size', 'price')
        read_only_fields = ('id',)
        
class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True) 
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='category.brand.name', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'name_en', 'name_ar', 'description_en', 
            'description_ar', 'image', 'variants', 'category_name', 
            'brand_name', 'created_at'
        )
        read_only_fields = ('category_name', 'brand_name', 'created_at', 'variants')
        extra_kwargs = {'image': {'required': False, 'allow_null': True}}


    def create(self, validated_data):
        variants_data = self.context.get('variants', [])        
        product = Product.objects.create(**validated_data)        
        for variant_data in variants_data:
            ProductVariant.objects.create(product=product, **variant_data)
            
        return product

    def update(self, instance, validated_data):
        validated_data.pop('variants', None)         
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.name_en = validated_data.get('name_en', instance.name_en)
        instance.name_ar = validated_data.get('name_ar', instance.name_ar)
        instance.description_en = validated_data.get('description_en', instance.description_en)
        instance.description_ar = validated_data.get('description_ar', instance.description_ar)
        
        instance.save()
        return instance