from django.contrib import admin
import xadmin
from goods.models import *

# Register your models here.
class GoodsAdmin(object):
    list_display = ['id', 'name', 'price', 'detail_name', 'pro_addr','goods_wheel_img']
    search_fields = ['name', 'category_name','child_name']
    list_filter = ['sale', 'stock']
    ordering = ('id',)
    list_cart_page = 30
    model_icon = 'fa fa-check-square'

class CategoryAdmin(object):
    list_display=['category_name','category_id']
    list_filter = ['category_name', 'category_id']
    search_field = ['category_name']
    ordering = ('category_id',)
    list_action_page = 30
    model_icon = 'fa fa-check-square'

class ChildAdmin(object):
    list_display=['child_name','child_id','category_id']
    list_filter = ['child_name','child_id', 'category_id']
    search_field = ['child_name']
    ordering = ('category_id',)
    list_action_page = 30
    model_icon = 'fa fa-check-square'

xadmin.site.register(YGGoods,GoodsAdmin)
xadmin.site.register(Child,ChildAdmin)
xadmin.site.register(Category,CategoryAdmin)