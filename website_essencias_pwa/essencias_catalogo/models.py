from django.db import models
from django.utils import timezone


def caminho_produto(instance, filename):
    return f"imagens/{instance.colecao.nome}/{filename}"

def caminho_colecao(instance, filename):
    return f"imagens/colecoes/{instance.nome}"

    
class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False)
    descricao = models.CharField(max_length=1000)
    imagem = models.ImageField(upload_to=caminho_colecao, blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Coleções"
    

class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False)
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=500)
    data_adicao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to=caminho_produto)

    def __str__(self):
        return self.nome
    
   