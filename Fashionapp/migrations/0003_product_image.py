# Generated by Django 4.2.2 on 2023-06-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fashionapp', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
