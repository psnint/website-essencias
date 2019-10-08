from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from .models import Produto


def index(request):
    return JsonResponse({"response": "Hello, world."})

def products(request):
    return JsonResponse({
        'catalogue' :[
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


class HomePageView(ListView):
    model = Produto
    template_name = 'public/main.js'
    
    def get_queryset(self):
        return Produto.objects.order_by('-data_adicao')
    
    
class DetailView(DetailView):
    model = Produto
    template_name = 'essencias_catalogo/detail.html'