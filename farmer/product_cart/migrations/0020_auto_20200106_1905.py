# Generated by Django 2.2.6 on 2020-01-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_cart', '0019_auto_20200106_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermanager',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='product_cart.OrderItem'),
        ),
        migrations.AlterField(
            model_name='ordermanager',
            name='orders',
            field=models.ManyToManyField(to='product_cart.Order'),
        ),
    ]
