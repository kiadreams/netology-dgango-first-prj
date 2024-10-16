from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


def index(request):
    return redirect('api/v1/products/')


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter,]
    search_fields = ['title', 'description',]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 1



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter,]
    filterset_fields = ['products',]
    search_fields = ['products__title', 'products__description',]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 1
