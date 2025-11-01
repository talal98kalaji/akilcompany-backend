from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

    # --- القفل ---
    # (يمنع الـ Superuser من إضافة ماركات جديدة من لوحة التحكم)
    def has_add_permission(self, request):
        return False

    # (يمنع الـ Superuser من حذف الماركات)
    def has_delete_permission(self, request, obj=None):
        return False