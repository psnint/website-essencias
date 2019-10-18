from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from django.core import serializers
from .models import Product, Collection


def index(request):
    data = serializers.serialize('json', Collection.objects.all())

    return HttpResponse(data, content_type="application/json")


def collection(request):
    if request.method == 'GET':
        collection_id = request.GET['collectionId']
        data = serializers.serialize('json', Collection.objects.filter(pk=collection_id))
        return HttpResponse(data, content_type="application/json")


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
