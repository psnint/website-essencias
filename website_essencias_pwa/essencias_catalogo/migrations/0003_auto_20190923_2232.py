# Generated by Django 2.2.5 on 2019-09-23 22:32

from django.db import migrations, models
import essencias_catalogo.models


class Migration(migrations.Migration):

    dependencies = [
        ('essencias_catalogo', '0002_auto_20190923_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colecao',
            name='imagem',
            field=models.ImageField(null=True, upload_to=essencias_catalogo.models.caminho_colecao),
        ),
    ]
