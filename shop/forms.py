from django.forms import ModelForm
from .models import good

class ListingForm(ModelForm):
    class Meta:
        model=good
        fields=['goods_title', 'goods_explanation', 'goods_remark','goods_quality','goods_price','preview1','preview2','preview3','preview4','category',]