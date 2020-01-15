from django.contrib import admin

# Register your models here.
from .models import Product, Collection, ProductImage

admin.site.register(Collection)
# admin.site.register(Product)
# admin.site.register(ProductImage)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    readonly_fields = ['image_tag']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
   

# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     pass