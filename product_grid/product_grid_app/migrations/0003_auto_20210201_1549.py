# Generated by Django 3.0.6 on 2021-02-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_grid_app', '0002_auto_20210201_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
