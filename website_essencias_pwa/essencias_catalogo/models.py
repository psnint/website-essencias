from django.db import models


def product_path(instance, filename):
    return f"images/{instance.collection.name}/{filename}"


def collection_path(instance, filename):
    return f"images/collections/{instance.nome}"


class Collection(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=collection_path, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Collections"


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    add_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=product_path)

    def __str__(self):
        return self.name
