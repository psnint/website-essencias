from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.generic import ListView, DetailView
from django.core import serializers

from .models import Product, Collection, ProductImage

import os
import zipfile
import json

from django.forms.models import model_to_dict


def __get_product_images(product_pk):
    product_images_objects = ProductImage.objects.filter(product=product_pk)
    product_images = [obj for obj in product_images_objects]
    return product_images


def index(request):
    data = serializers.serialize('json', Collection.objects.all())
    response = HttpResponse(data, content_type="application/json")

    return response


def __get_collection_and_products(collection_id):
    # Get collection and respective products
    collection = Collection.objects.filter(pk=collection_id)
    collection_products = Product.objects.filter(collection=collection_id)

    # Transform objects into a dictionary
    collection_data = json.loads(serializers.serialize('json', collection))[0]
    collection_products_data = json.loads(serializers.serialize('json', collection_products))

    # Append the all products information to the collection
    collection_data['products'] = collection_products_data

    for product in collection_data['products']:
        # Get image paths only
        product['images'] = [{'id': img.id, 'url': img.image.url} for img in __get_product_images(product['pk'])]

    response = json.dumps(collection_data, ensure_ascii=False)
    return HttpResponse(response, content_type="application/json")


def collection(request):
    if request.method == 'GET':
        collection_id = request.GET['collectionId']
        return __get_collection_and_products(collection_id)


def download_collection(request):
    if request.method == 'GET':

        # Get collection products
        lang = request.GET['lang']
        collection_id = request.GET['collectionId']
        collection_products = Product.objects.filter(collection=collection_id)

        # Get or create tmp dir for creating the zip file
        tmp_dir = os.path.join('media', 'tmp')
        os.makedirs(tmp_dir, exist_ok=True)

        # Delete zipfile if it exists already
        collection_name = getattr(Collection.objects.get(pk=collection_id), 'name_{}'.format(lang))
        zipfile_name = '{}.zip'.format(collection_name)
        zipfile_path = os.path.join(tmp_dir, zipfile_name)
        if os.path.isfile(zipfile_path):
            os.remove(zipfile_path)

        # Zip images
        with zipfile.ZipFile(zipfile_path, 'w', zipfile.ZIP_DEFLATED) as zipfile_handler:
            for product in collection_products:
                product_images = __get_product_images(product.pk)

                # Write each image of the product to the zip file
                for product_image in product_images:
                    zipfile_handler.write(product_image.image.path,
                                          os.path.basename(product_image.image.path))

        # Send attachment
        with open(zipfile_path, 'rb') as collection_zip:
            response = HttpResponse(collection_zip, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(zipfile_name)

        # Delete zip file
        if os.path.isfile(zipfile_path):
            os.remove(zipfile_path)
        return response


def download_product(request):
    if request.method == 'GET':
        product_id = request.GET['productId']
        product_image_index = int(request.GET['productImage'])

        product_image = ProductImage.objects.filter(product=product_id)[product_image_index]

        response = HttpResponse(product_image.image, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.basename(product_image.image.path))
        return response


def product_collection(request):
    if request.method == 'GET':
        product_id = request.GET['productId']
        product = Product.objects.filter(pk=product_id)[0]
        collection_id = product.collection.id
        return __get_collection_and_products(collection_id)


def products(request):
    return JsonResponse({
        'catalogue': [
            {
                'name': 'Sentidos',
                'imgUrl': 'media/imagens/mockCollection/mock1.png',
            },
            {
                'name': 'Essencia',
                'imgUrl': 'media/imagens/mockCollection/mock2.png',
            },
            {
                'name': 'Essencia',
                'imgUrl': 'media/imagens/mockCollection/mock3.png',
            },
            {
                'name': 'Essencia',
                'imgUrl': 'media/imagens/mockCollection/mock1.png',
            },
            {
                'name': 'Teste',
                'imgUrl': 'media/imagens/mockCollection/mock2.png',
            },
            {
                'name': 'Frutis',
                'imgUrl': 'media/imagens/mockCollection/mock3.png',
            },
        ],
    })
