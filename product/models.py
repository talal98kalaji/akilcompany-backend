# product/models.py
from django.db import models
from category.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Type")    
    name_en = models.CharField(max_length=255, verbose_name="English Name")
    name_ar = models.CharField(max_length=255, verbose_name="Arabic Name")
    description_en = models.TextField(blank=True, null=True, verbose_name="English Description")
    description_ar = models.TextField(blank=True, null=True, verbose_name="Arabic Description")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="product image")    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']

    def __str__(self):
        return self.name_en


class ProductVariant(models.Model):
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', '3XL'),
        ('XXXXL', '4XL'),
    ]
    
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE, verbose_name="المنتج")
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, verbose_name="المقاس")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    
    class Meta:
        verbose_name = "Product Variant"
        verbose_name_plural = "Product Variants"
        unique_together = ('product', 'size')
        ordering = ['price']

    def __str__(self):
        return f"{self.product.name_en} - {self.size} ({self.price})"