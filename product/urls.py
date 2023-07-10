from django.urls import path
from .views import  LatestProductsList, ProductList, ProductDetail

urlpatterns = [
    path('latest-products/', LatestProductsList.as_view(), name='latest_products'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product_detail'),

]