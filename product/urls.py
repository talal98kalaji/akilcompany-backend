# product/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('all/', views.get_all_products, name='product-list'),
    path('create/', views.create_product, name='product-create'),
    path('detail/<int:pk>/', views.get_product_by_id, name='product-detail'),
    path('update/<int:pk>/', views.update_product, name='product-update'),
    path('delete/<int:pk>/', views.delete_product, name='product-delete'),
]