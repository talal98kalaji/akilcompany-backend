# category/models.py
from django.db import models
from brand.models import Brand 

class Category(models.Model):
    brand = models.ForeignKey(Brand, related_name='categories', on_delete=models.CASCADE, verbose_name="Brand")
    name = models.CharField(max_length=50, verbose_name="category name") 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        unique_together = ('brand', 'name') 
        ordering = ['brand__name', 'name']

    def __str__(self):
        return f"{self.brand.name} - {self.name}"