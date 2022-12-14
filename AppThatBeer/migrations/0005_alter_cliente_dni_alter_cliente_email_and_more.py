# Generated by Django 4.1 on 2022-08-26 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppThatBeer', '0004_rename_nombre_bar_distribuidor_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='distribuidor',
            name='cuit',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='patrocinador',
            name='web',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
