# Generated by Django 4.2.4 on 2023-10-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0007_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
