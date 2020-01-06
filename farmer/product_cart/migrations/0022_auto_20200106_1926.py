# Generated by Django 2.2.6 on 2020-01-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_cart', '0021_auto_20200106_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='orderItemCode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='product_cart.OrderItem'),
        ),
    ]