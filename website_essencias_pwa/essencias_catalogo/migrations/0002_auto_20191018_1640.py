# Generated by Django 2.2.5 on 2019-10-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essencias_catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='description',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='collection',
            name='description_en',
            field=models.CharField(default='No description.', max_length=1000),
        ),
        migrations.AddField(
            model_name='collection',
            name='description_fr',
            field=models.CharField(default='Pas de description.', max_length=1000),
        ),
        migrations.AddField(
            model_name='collection',
            name='description_pt',
            field=models.CharField(default='Sem descrição.', max_length=1000),
        ),
        migrations.AddField(
            model_name='collection',
            name='name_en',
            field=models.CharField(default='english_name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='name_fr',
            field=models.CharField(default='nom français', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='name_pt',
            field=models.CharField(default='nome portugues', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.CharField(default='No description.', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='description_fr',
            field=models.CharField(default='Pas de description.', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='description_pt',
            field=models.CharField(default='Sem descrição.', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(default='english name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name_fr',
            field=models.CharField(default='nom français', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name_pt',
            field=models.CharField(default='nome portugues', max_length=100),
            preserve_default=False,
        ),
    ]