# Generated by Django 2.2.5 on 2019-09-23 22:29

from django.db import migrations, models
import django.db.models.deletion
import essencias_catalogo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.CharField(max_length=1000)),
                ('imagem', models.ImageField(upload_to=essencias_catalogo.models.caminho_colecao)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.CharField(max_length=500)),
                ('data_adicao', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(upload_to=essencias_catalogo.models.caminho_produto)),
                ('colecao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essencias_catalogo.Colecao')),
            ],
        ),
    ]
