#from django.contrib import admin
from order.models import *
import xadmin

# Register your models here.
class OrderAdmin(object):
    list_display = ['id', 'o_user', 'o_price', 'o_status']
    search_fields = ['o_user','o_status']
    list_filter = ['update_time', 'create_time','o_status']
    ordering = ('id',)
    list_order_page = 30
    model_icon = 'fa fa-check-square'

class CartAdmin(object):
    list_display = ['c_user', 'c_goods', 'total_price']
    search_fields = ['c_user']
    list_filter = ['c_user', 'c_goods']
    ordering = ('id',)
    list_cart_page = 30
    model_icon = 'fa fa-check-square'

class AddressAdmin(object):
    list_display = ['address_details']
    list_filter = ['phone_num','addr_type']
    search_field = ['name']
    ordering = ('id',)
    list_addr_page = 30
    model_icon = 'fa fa-check-square'

class OrderDetailAdmin(object):
    list_display = ['o_order', 'o_goods', 'o_goods_num']
    list_filter = ['o_order', 'o_goods','o_goods_num']
    search_field = ['o_order']
    ordering = ('id',)
    list_orddet_page = 30
    model_icon = 'fa fa-check-square'

class CommentAdmin(object):
    list_display = ['user', 'order_id', 'comments']
    list_filter = ['user']
    search_field = ['user','comments']
    ordering = ('id',)
    list_comment_page = 30
    model_icon = 'fa fa-check-square'

xadmin.site.register(YGOrder,OrderAdmin)
xadmin.site.register(YGOderDetail,OrderDetailAdmin)
xadmin.site.register(YGCart,CartAdmin)
xadmin.site.register(YGComment,CommentAdmin)
xadmin.site.register(YGAddress,AddressAdmin)