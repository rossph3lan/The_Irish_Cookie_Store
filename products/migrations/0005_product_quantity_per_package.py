# Generated by Django 4.0.1 on 2022-01-29 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_flavour_images_flavourimage_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_per_package',
            field=models.IntegerField(default=1),
        ),
    ]
