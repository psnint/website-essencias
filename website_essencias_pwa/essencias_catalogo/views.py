from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.generic import ListView, DetailView
from django.core import serializers

from .models import Product, Collection

import os
import zipfile
import json

from django.forms.models import model_to_dict



def index(request):
    data = serializers.serialize('json', Collection.objects.all())

    return HttpResponse(data, content_type="application/json")


def collection(request):
    if request.method == 'GET':
        collection_id = request.GET['collectionId']
        
        # Get collection and respective products
        collection = Collection.objects.filter(pk=collection_id)
        collection_products = Product.objects.filter(collection=collection_id)
        
        # Transform objects into a dictionary
        collection_data = json.loads(serializers.serialize('json', collection))[0]
        collection_products_data = json.loads(serializers.serialize('json', collection_products))
        
        # Append the all products information to the collection
        collection_data['products'] = collection_products_data
        
        response = json.dumps(collection_data, ensure_ascii=False)
        return HttpResponse(response, content_type="application/json")


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
                zipfile_handler.write(product.image.path,  # actual image file
                                      os.path.basename(product.image.path))  # image file "path" to be zipped

        # Send attachment
        with open(zipfile_path, 'rb') as collection_zip:
            response = HttpResponse(collection_zip, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(zipfile_name)

        # Delete zip file
        if os.path.isfile(zipfile_path):
            os.remove(zipfile_path)

        return response


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
