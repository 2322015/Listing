# Generated by Django 4.0 on 2023-11-06 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_goods_good'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='goods_id',
        ),
    ]
