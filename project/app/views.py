from django.shortcuts import render
from .models import Product, Category
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProductSerializer, CategorySerializer
from django.http import JsonResponse


# Create your views here.
class ProductList(APIView):
    def get(self, request, format=None):
        all_product = Product.objects.all()
        serializers = ProductSerializer(all_product, many=True)
        return Response(serializers.data)


class CategoryList(APIView):
    def get(self, request, format=None):
        all_categories = Category.objects.all()
        serializers = CategorySerializer(all_categories, many=True)
        return Response(serializers.data)


class SubcategoryList(APIView):
    def get(self, request, parent_id, format=None):
        parent_category = Category.objects.get(id=parent_id)
        subcategories = parent_category.child.all()
        serializer = CategorySerializer(subcategories, many=True)
        return Response(serializer.data)


def get_parent_id_by_category_name(request):
    category_name = request.GET.get('category_name')
    try:
        category = Category.objects.get(name=category_name)
        parent_id = category.parent_id
        return JsonResponse({'parent_id': parent_id})
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)


def get_category_id(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
        category_id = category.id
        return JsonResponse({'category_id': category_id})
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)