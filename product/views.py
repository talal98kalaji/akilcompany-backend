# product/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer, ProductVariantSerializer 
import json 

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_products(request):
    queryset = Product.objects.all().select_related('category', 'category__brand').prefetch_related('variants')
    category_id = request.query_params.get('category_id', None)
    if category_id is not None:
        queryset = queryset.filter(category__id=category_id)

    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def create_product(request):
    variants_string = request.data.get('variants', '[]')
    try:
        variants_data = json.loads(variants_string)
        if not isinstance(variants_data, list):
            raise json.JSONDecodeError            
    except json.JSONDecodeError:
        return Response(
            {'error': 'Invalid JSON format for variants. Must be a JSON array string.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    variant_serializer = ProductVariantSerializer(data=variants_data, many=True)
    if not variant_serializer.is_valid():
        return Response(
            {'variant_errors': variant_serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    serializer = ProductSerializer(
        data=request.data, 
        context={'variants': variant_serializer.validated_data}
    )
    
    if serializer.is_valid():
        serializer.save()
        response_serializer = ProductSerializer(serializer.instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_product_object(pk):
    try:
        return Product.objects.select_related('category', 'category__brand').prefetch_related('variants').get(pk=pk)
    except Product.DoesNotExist:
        return None

@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_by_id(request, pk):
    product = get_product_object(pk)
    if product is None:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_product(request, pk):
    product = get_product_object(pk)
    if product is None:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    partial = True if request.method == 'PATCH' else False
    
    serializer = ProductSerializer(product, data=request.data, partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_product(request, pk):
    product = get_product_object(pk)
    if product is None:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)        
    product.delete()
    return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)