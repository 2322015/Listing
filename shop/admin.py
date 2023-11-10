from django.contrib import admin
from .models import good,Category

class goodmodels(admin.ModelAdmin):
    list_display=('id','goods_title', 'category','user','goods_quality',)
    list_display_links=('id','goods_title', 'category','user','goods_quality',)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'title')
    list_display_links=('id', 'title')
    
# Register your models here.
admin.site.register(good,goodmodels)
admin.site.register(Category, CategoryAdmin)