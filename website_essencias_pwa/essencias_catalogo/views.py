from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from .models import Produto


def index(request):
    return JsonResponse({"response": "Hello, world."})


class HomePageView(ListView):
    model = Produto
    template_name = 'public/main.js'
    
    def get_queryset(self):
        return Produto.objects.order_by('-data_adicao')
    
    
class DetailView(DetailView):
    model = Produto
    template_name = 'essencias_catalogo/detail.html'