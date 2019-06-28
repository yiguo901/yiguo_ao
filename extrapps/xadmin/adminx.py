from __future__ import absolute_import
import xadmin
# Register your models here.
from mainapp.models import *
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '易果生鲜管理系统'
    site_footer = '个人网站'
    site_url = '/'
    menu_style = 'accordion'


class UserAdmin(object):
    list_display = ['id','u_phone','nickname','level',
                    'gender','u_auth_string','idcard','img']
    search_fields = ['nickname','gender']
    list_filter = ['nickname','level','gender']
    ordering = ('id',)
    list_per_page = 30
    model_icon = 'fa fa-check-square'

class OrderAdmin(object):
    list_display = ['id', 'o_user', 'o_price', 'o_time','o_status']
    search_fields = ['o_user', 'o_time','o_status']
    list_filter = ['o_user', 'o_time','o_status']
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

class GoodsAdmin(object):
    list_display = ['id', 'name', 'price', 'detail_name', 'pro_addr','goods_wheel_img']
    search_fields = ['name', 'category_name','child_name']
    list_filter = ['sale', 'stock']
    ordering = ('id',)
    list_cart_page = 30
    model_icon = 'fa fa-check-square'


class WheelAdmin(object):
    list_display = ['img_url', 'img_name']
    list_filter = ['img_name']
    search_field = ['img_name']
    ordering = ('id',)
    list_wheel_page = 30
    model_icon = 'fa fa-check-square'

class ChosenAdmin(object):
    list_display = ['img_url', 'img_name']
    list_filter = ['img_name']
    search_field = ['img_name']
    ordering = ('id',)
    list_addr_page = 30
    model_icon = 'fa fa-check-square'

class NavAdmin(object):
    list_display = ['img_url', 'img_name']
    list_filter = ['img_name']
    search_field = ['img_name']
    ordering = ('id',)
    list_addr_page = 30
    model_icon = 'fa fa-check-square'

class NavDetailAdmin(object):
    list_display = ['img_url', 'img_name']
    list_filter = ['img_name']
    search_field = ['img_name']
    ordering = ('id',)
    list_addr_page = 10
    model_icon = 'fa fa-check-square'

class AddressAdmin(object):
    list_display = ['address','add_time']
    list_filter = ['add_time']
    search_field = ['address']
    ordering = ('add_time',)
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

class EatAdmin(object):
    list_display = ['id', 'eat_img', 'eat_contribute','action_time','action_name']
    list_filter = ['id', 'action_name']
    search_field = ['id','action_name']
    ordering = ('action_time',)
    list_action_page = 30
    model_icon = 'fa fa-check-square'

xadmin.site.register(YGUser,UserAdmin)
xadmin.site.register(YGGoods,GoodsAdmin)
xadmin.site.register(YGOrder,OrderAdmin)
xadmin.site.register(YGOderDetail,OrderDetailAdmin)
xadmin.site.register(YGCart,CartAdmin)
xadmin.site.register(YGNav,NavAdmin)
xadmin.site.register(YGWheel,WheelAdmin)
xadmin.site.register(YGComment,CommentAdmin)
xadmin.site.register(YGAddress,AddressAdmin)
xadmin.site.register(YGNavDetail,NavDetailAdmin)
xadmin.site.register(YGChosen,ChosenAdmin)
xadmin.site.register(YGEat,EatAdmin)

xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting)