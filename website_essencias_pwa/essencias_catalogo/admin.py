from django.contrib import admin
from django.utils.html import mark_safe

# Register your models here.
from .models import Product, Collection, ProductImage


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    readonly_fields = ['image_tag']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    list_display = ("name_pt", "description_pt", "collection", "add_date", "image_display")
    list_filter = ("collection", "add_date",)
    search_fields = ('name_pt', )


    def image_display(self, obj):
        first_image = ProductImage.objects.filter(product=obj)[0]
        return mark_safe(f'<img src="/{first_image.image.url}" width="50" height="50" />')

    image_display.allow_tags = True
    image_display.__name__ = "Image"
   

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ['image_tag']
    list_display = ("name_pt", "description_pt", "add_date", "image_display",)
    list_filter = ("name_pt", "add_date", )
    search_fields = ('name_pt', )

    def image_display(self, obj):
        return mark_safe(f'<img src="/{obj.image.url}" width="50" height="50" />')

    image_display.allow_tags = True
    image_display.__name__ = "Image"
