# Generated by Django 2.2.5 on 2019-10-08 19:06

from django.db import migrations, models
import django.db.models.deletion
import essencias_catalogo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to=essencias_catalogo.models.collection_path)),
            ],
            options={
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=essencias_catalogo.models.product_path)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essencias_catalogo.Collection')),
            ],
        ),
    ]
