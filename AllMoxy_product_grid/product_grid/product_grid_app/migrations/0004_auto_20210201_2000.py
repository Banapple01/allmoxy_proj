# Generated by Django 3.0.6 on 2021-02-02 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_grid_app', '0003_auto_20210201_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.TextField(),
        ),
    ]
