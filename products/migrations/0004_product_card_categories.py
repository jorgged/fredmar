# Generated by Django 2.0 on 2018-05-19 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180519_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_card',
            name='categories',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
