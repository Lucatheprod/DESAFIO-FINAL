# Generated by Django 4.1.1 on 2022-09-21 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppThatBeer', '0018_alter_noticia_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='cuerpo',
            field=models.CharField(max_length=3000),
        ),
    ]
