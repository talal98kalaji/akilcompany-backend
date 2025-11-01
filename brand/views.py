from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
from rest_framework import status
from .models import Brand
from .serializers import BrandSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_brands(request):
    queryset = Brand.objects.all()
    search_name = request.query_params.get('name', None)
    if search_name is not None:
        queryset = queryset.filter(name__icontains(search_name))

    serializer = BrandSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_brand_by_id(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return Response({'error': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BrandSerializer(brand)
    return Response(serializer.data, status=status.HTTP_200_OK)