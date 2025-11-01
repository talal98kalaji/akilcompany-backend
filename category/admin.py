# category/admin.py
from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # عرض الحقول المرتبطة بشكل جيد
    list_display = ('name', 'brand') 
    # إضافة فلتر سهل للوصول
    list_filter = ('brand',) 
    search_fields = ('name',)

    # --- القفل ---
    # (يمنع الـ Superuser من إضافة أصناف جديدة من لوحة التحكم)
    def has_add_permission(self, request):
        return False
        
    # (يمنع الـ Superuser من حذف الأصناف)
    def has_delete_permission(self, request, obj=None):
        return False