# category/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny # (السماح للزوار بالقراءة)
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

# ---------------------------------
# 1. GET (List) + Filter by Brand
# ---------------------------------
@api_view(['GET'])
@permission_classes([AllowAny]) # <-- السماح للجميع بالقراءة
def get_all_categories(request):
    """
    جلب كل الأصناف مع إمكانية الفلترة حسب الماركة
    (e.g., /api/category/all/?brand_id=1)
    """
    # .select_related('brand') لتحسين الأداء (يمنع N+1 query)
    queryset = Category.objects.all().select_related('brand')

    # (الفلتر)
    brand_id = request.query_params.get('brand_id', None)
    if brand_id is not None:
        queryset = queryset.filter(brand__id=brand_id)

    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# ---------------------------------
# 2. GET (Retrieve by ID)
# ---------------------------------
@api_view(['GET'])
@permission_classes([AllowAny]) # <-- السماح للجميع بالقراءة
def get_category_by_id(request, pk):
    """
    جلب صنف واحد عن طريق الـ ID
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)