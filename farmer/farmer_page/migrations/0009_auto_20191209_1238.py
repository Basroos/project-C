# Generated by Django 2.2.5 on 2019-12-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_page', '0008_auto_20191209_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='fullname',
            field=models.CharField(default='ome henk', max_length=44, null=True),
        ),
    ]
