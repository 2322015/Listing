# Generated by Django 4.0 on 2023-11-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_goods_goods_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.CharField(choices=[('game', 'ゲーム'), ('anime', 'アニメ'), ('comic', '漫画'), ('fan_magazine', '同人誌'), ('CD', 'CD')], default=1, max_length=50, verbose_name='カテゴリ'),
            preserve_default=False,
        ),
    ]
