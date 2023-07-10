from django.contrib import admin

# Register your models here.
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['id', 'name', 'description', 'slug', 'created_date']
    list_filter = ['created_date']
    list_editable = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['created_date']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['id','category', 'name', 'description', 'slug', 'price', 'stock', 'is_available', 'created_date']
    list_filter = ['created_date', 'category']
    list_editable = ['category','name', 'description', 'price', 'stock', 'is_available']
    search_fields = ['name', 'description', 'category__name']
    ordering = ['created_date']

admin.site.register(Product, ProductAdmin)
