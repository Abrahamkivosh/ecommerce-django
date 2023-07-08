from typing import Any
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(black=True, null=True)
    image = models.ImageField(upload_to='category', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name')

class Product(models.Model):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.base_url = "http://127.0.0.1:8000"

    name = models.CharField(max_length=200)
    description = models.TextField(black=True, null=True)
    image = models.ImageField(upload_to='product', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='product', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return self.base_url + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.base_url + self.thumbnail.url
        else:
            if self.image:
                return self.base_url + self.image.url
            else:
                if self.image:
                    self.thumbnail = self.make_thumbnail(self.image)
                    self.save()
                    return self.base_url + self.thumbnail.url
                else:
                    return ''
    def make_thumbnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
                
        

