# Generated by Django 4.1 on 2022-10-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storesinfo', '0005_kmeans_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kmeans',
            name='clustersNumber',
            field=models.IntegerField(),
        ),
    ]