# Generated by Django 4.0 on 2023-11-06 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_group'),
        ('shop', '0006_remove_good_goods_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser', verbose_name='出品者'),
        ),
    ]
