from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="brand name")
    image = models.ImageField(upload_to='brand/images/', null=True, blank=True, verbose_name="شعار الماركة")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"
        ordering = ['name'] 

    def __str__(self):
        return self.name