# Generated by Django 2.0.3 on 2019-12-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_cart', '0010_auto_20191216_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='product_cart.OrderItem'),
        ),
    ]
