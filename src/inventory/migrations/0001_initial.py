# Generated by Django 3.0.2 on 2020-01-15 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mfg_name', models.CharField(blank=True, max_length=300, verbose_name='Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='StockStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_stage', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Stock Status',
            },
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor_name', models.CharField(max_length=300, verbose_name='Item')),
                ('item_stock_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.StockStatus', verbose_name='Stock Status')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=300, verbose_name='Product')),
                ('item_location', models.CharField(blank=True, max_length=300, null=True, verbose_name='Location')),
                ('item_active', models.BooleanField(default=False, verbose_name='Active')),
                ('slug', models.SlugField()),
                ('item_manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Manufacturer', verbose_name='Manufacturer')),
                ('item_stock_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.StockStatus', verbose_name='Stock Status')),
            ],
        ),
    ]