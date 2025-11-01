from django.urls import path
from . import views 

urlpatterns = [
    path('all/', views.get_all_brands, name='brand-list'),
    path('detail/<int:pk>/', views.get_brand_by_id, name='brand-detail'),
]