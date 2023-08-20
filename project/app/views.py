from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProductSerializer


# Create your views here.
class ProductList(APIView):
    def get(self, request, format=None):
        all_product = Product.objects.all()
        serializers = ProductSerializer(all_product, many=True)
        return Response(serializers.data)
