# Generated by Django 4.1.1 on 2022-09-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canalmensaje',
            name='texto',
            field=models.CharField(max_length=4500),
        ),
    ]
