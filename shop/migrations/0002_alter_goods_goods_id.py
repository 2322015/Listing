# Generated by Django 4.0 on 2023-11-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_id',
            field=models.CharField(max_length=200, verbose_name='商品ID'),
        ),
    ]
