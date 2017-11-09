from django.shortcuts import render
from rest_framework.decorators import detail_route
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models


class ProductCreateAPIView(CreateAPIView, ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.ProductsSerializers
    model = models.Product
    queryset = models.Product.objects.all()

    def get_queryset(self, *args, **kwargs):
        return models.Product.objects.all()


class ProductUpdateAPIView(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializers.ProductsSerializers
    # model = models.Product
    queryset = models.Product.objects.all()


class CategoryCreateAPIView(ListAPIView, CreateAPIView):
    serializer_class = serializers.CategorySerializers
    # model = models.Category
    queryset = models.Category.objects.all()


class CategoryUpdateAPIView(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializers.CategorySerializers
    # model = models.Category
    queryset = models.Category.objects.all()

    @detail_route(url='custom')
    def some_def(self):
        pass

class ProductViewSet(ModelViewSet):
    """Show some things about product"""
    serializer_class = serializers.ProductsSerializers
    queryset = models.Product.objects.all()


class CategoryViewSet(ModelViewSet):
    """Show some things about category"""
    serializer_class = serializers.CategorySerializers
    queryset = models.Category.objects.all()









# from django.shortcuts import render
# from rest_framework.generics import ListAPIView
# from .serializers import ProductsSerializers, CategorySerializers
#
# from .models import Product, Category
#
#
# class ProductView(ListAPIView):
#     serializer_class = ProductsSerializers
#     model = Product
#     queryset = Product.objects.all()
#
#
# class CategoryView(ListAPIView):
#     serializer_class = CategorySerializers
#     model = Category
#     queryset = Category.objects.all()

