# Generated by Django 2.2.5 on 2020-01-14 10:47

from django.db import migrations, models
import django.db.models.deletion
import essencias_catalogo.models


class Migration(migrations.Migration):

    dependencies = [
        ('essencias_catalogo', '0002_auto_20191018_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=essencias_catalogo.models.product_path)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essencias_catalogo.ProductImage'),
        ),
    ]
