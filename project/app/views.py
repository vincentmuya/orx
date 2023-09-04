from django.shortcuts import render,get_object_or_404
from .models import Product, Category
from rest_framework.views import APIView
from .serializer import ProductSerializer, CategorySerializer, NewProductSerializer
from django.http import JsonResponse
from .forms import NewProduct
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
class ProductList(APIView):
    def get(self, request, format=None):
        category_id = request.query_params.get('category_id')

        if category_id is not None:
            products = Product.objects.filter(category=category_id)
        else:
            products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


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


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    serializer = ProductSerializer(product)
    return JsonResponse(serializer.data)


# @csrf_exempt
# def new_product(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProduct(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.seller = current_user
#             product.save()
#             # Return a success response
#             return JsonResponse({'message': 'Product created successfully'})
#         else:
#             # Return an error response with form errors
#             errors = form.errors.as_json()
#             return JsonResponse({'errors': errors}, status=400)
#     else:
#         # Return an error response for non-POST requests
#         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
#

class NewProductAPIView(APIView):
    def post(self, request):
        serializer = NewProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the data to the database
            return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_form_fields(request):
    # Define the form fields and their default values
    form_fields = {
        'title': '',
        'description': '',
        'price': None,
        'category': None,  # You may need to specify a default category ID or None based on your requirements
        'image': None,
    }

    return Response(form_fields)