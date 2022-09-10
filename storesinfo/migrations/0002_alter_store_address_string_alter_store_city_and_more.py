# Generated by Django 4.1 on 2022-09-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storesinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address_string',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='country',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='country_code',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='fri_open_hours',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='latitude',
            field=models.FloatField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='longitude',
            field=models.FloatField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='mon_open_hours',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='sat_open_hours',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='state',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_class',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='store',
            name='streetName1',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='streetName2',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='sun_open_hours',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='thu_open_hours',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='tue_open_hours',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='wed_open_hours',
            field=models.CharField(max_length=50, null=True),
        ),
    ]