# product/admin.py
from django.contrib import admin
from .models import Product, ProductVariant

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ar', 'category', 'created_at')
    list_filter = ('category__brand', 'category')
    search_fields = ('name_en', 'name_ar')
    autocomplete_fields = ['category']    
    inlines = [ProductVariantInline]

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'price')
    list_filter = ('product__category__brand', 'size')
    search_fields = ('product__name_en',)