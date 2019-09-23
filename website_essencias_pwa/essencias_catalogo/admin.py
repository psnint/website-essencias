from django.contrib import admin

# Register your models here.
from .models import Produto, Colecao

admin.site.register(Colecao)
admin.site.register(Produto)