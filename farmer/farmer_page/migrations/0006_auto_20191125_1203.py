# Generated by Django 2.2.7 on 2019-11-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_page', '0005_auto_20191112_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='age',
            field=models.CharField(max_length=2),
        ),
    ]