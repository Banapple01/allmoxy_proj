# Generated by Django 3.0.6 on 2021-02-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_grid_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
