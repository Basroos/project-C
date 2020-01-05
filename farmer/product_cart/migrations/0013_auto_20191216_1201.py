# Generated by Django 2.0.3 on 2019-12-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_cart', '0012_auto_20191216_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='subTotal',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='product_cart.OrderItem'),
        ),
    ]