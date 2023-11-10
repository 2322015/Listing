from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Category(models.Model):
    title=models.CharField(
        verbose_name='カテゴリ',
        max_length=20)
    def __str__(self) -> str:
        return self.title


class good(models.Model):

    CATEGORY=(('ゲーム', 'ゲーム'),
                ('アニメ', 'アニメ'),
                ('漫画', '漫画'),
                ('同人誌', '同人誌'),
                ('CD', 'CD'),
                ('機械', '機械'),
                ('その他','その他'))

    
    QUALITY=(('未使用', '未使用'),
                ('非常に良い', '非常に良い'),
                ('良い', '良い'),
                ('普通', '普通'),
                ('悪い', '悪い'),
                ('非常に悪い', '非常に悪い'))

    user=models.ForeignKey(
        CustomUser,

        verbose_name='出品者',

        on_delete=models.CASCADE
    )

    goods_title = models.TextField(
        verbose_name = '商品名')
    category= models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        choices=CATEGORY
    )
    goods_explanation=models.TextField(null=True, blank=True,
        verbose_name='説明')
    goods_remark=models.TextField(null=True, blank=True,
        verbose_name='備考')
    goods_quality=models.TextField(
        verbose_name='品質',
        choices=QUALITY)
    goods_price=models.TextField(
        verbose_name='価格'
    )
    preview1=models.FileField(verbose_name='写真1',
                                upload_to='photos',
                                null=True,
                                blank=True
                                )
    preview2=models.FileField(verbose_name='写真2',
                                upload_to='photos',
                                blank=True,
                                null=True
                                )
    preview3=models.FileField(verbose_name='写真3',
                                upload_to='photos',
                                blank=True,
                                null=True
                                )
    preview4=models.FileField(verbose_name='写真4',
                                upload_to='photos',
                                blank=True,
                                null=True
                                )

    review=models.TextField(
        verbose_name='レビュー',
        blank=True,
        null=True
        )



