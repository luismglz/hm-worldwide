# Generated by Django 4.1 on 2022-10-19 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storesinfo', '0004_alter_store_store_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='KMeans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clustersNumber', models.IntegerField(max_length=55)),
                ('tolerance', models.FloatField()),
                ('numberIterations', models.IntegerField()),
                ('clusterStd', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitudeRange', models.FloatField(max_length=50)),
                ('latitudeRange', models.FloatField(max_length=50)),
                ('samplesNumber', models.IntegerField()),
                ('clusterStd', models.FloatField()),
            ],
        ),
    ]
