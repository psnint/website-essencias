from django.contrib import admin

# Register your models here.
from .models import Product, Collection

admin.site.register(Collection)
admin.site.register(Product)
