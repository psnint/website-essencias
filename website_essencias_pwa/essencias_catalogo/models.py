from django.db import models
from django.utils.html import mark_safe
import ntpath


def product_path(instance, filename):
    return f"images/collections/{instance.product.collection.name_pt}/products/{filename}"


def collection_path(instance, filename):
    return f"images/collections/{instance.name_pt}/{filename}"


class Collection(models.Model):
    name_pt = models.CharField(max_length=100, verbose_name="Nome")
    name_en = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)

    description_pt = models.CharField(max_length=1000, default='Sem descrição.')
    description_en = models.CharField(max_length=1000, default='No description.')
    description_fr = models.CharField(max_length=1000, default='Pas de description.')

    image = models.ImageField(upload_to=collection_path, blank=True, null=True)

    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_pt

    def image_tag(self):
        """
        Used to display an image in the admin panel.
        """
        return mark_safe(f'<img src="/{self.image.url}" width="150" height="150" />')

    image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = "Collections"

   


class Product(models.Model):
    name_pt = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    description_pt = models.CharField(max_length=1000, default='Sem descrição.')
    description_en = models.CharField(max_length=1000, default='No description.')
    description_fr = models.CharField(max_length=1000, default='Pas de description.')

    add_date = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to=product_path)
    def __str__(self):
        return self.name_pt


class ProductImage(models.Model):
    """
    Class for the actual image file in a product.
    Needed so that a Product can have multiple ProductImage.
    It's the image that knows which products it belongs to, and not vice-versa.
    """

    image = models.ImageField(upload_to=product_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.product.name_pt + " (" + ntpath.basename(self.image.path) + ")"

    def image_tag(self):
        """
        Used to display an image in the admin panel.
        """
        return mark_safe(f'<img src="/{self.image.url}" width="150" height="150" />')

    image_tag.short_description = 'Image'
