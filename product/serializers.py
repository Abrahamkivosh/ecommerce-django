from rest_framework import serializers, viewsets, routers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'get_image', 'get_absolute_url']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    category = CategorySerializer(many=False, read_only=True, required=False, allow_null=True)
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'get_image',
                  'get_thumbnail',
                  'get_absolute_url', 'price', 'stock', 'is_available'
                  ]
        read_only_fields = ['id']

        