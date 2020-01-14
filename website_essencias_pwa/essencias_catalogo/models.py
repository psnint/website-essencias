from django.db import models


def product_path(instance, filename):
    return f"images/collections/{instance.collection.name_pt}/products/{filename}"


def collection_path(instance, filename):
    return f"images/collections/{instance.name_pt}/{filename}"


class Collection(models.Model):
    name_pt = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)

    description_pt = models.CharField(max_length=1000, default='Sem descrição.')
    description_en = models.CharField(max_length=1000, default='No description.')
    description_fr = models.CharField(max_length=1000, default='Pas de description.')

    image = models.ImageField(upload_to=collection_path, blank=True, null=True)

    def __str__(self):
        return self.name_pt

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
    image = models.ImageField(upload_to=product_path)

    def __str__(self):
        return self.name_pt
