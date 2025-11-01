# category/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    # (GET) /api/category/all/
    # (GET) /api/category/all/?brand_id=1
    path('all/', views.get_all_categories, name='category-list'),
    
    # (GET) /api/category/detail/<id>/
    path('detail/<int:pk>/', views.get_category_by_id, name='category-detail'),
]