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

class YGMainAdmin(object):
    pass


class UserAdmin(object):
    list_display = ['id','u_phone','nickname','level',
                    'gender','u_auth_string','idcard']
    search_fields = ['nickname','gender']
    list_filter = ['nickname','level','gender']
    ordering = ('id',)
    list_per_page = 30
    model_icon = 'fa fa-check-square'

class OrderAdmin(object):
    pass

class CartAdmin(object):
    pass

class GoodsAdmin(object):
    pass


class WheelAdmin(object):
    pass

class ChosenAdmin(object):
    pass

class NavAdmin(object):
    pass

class NavDetailAdmin(object):
    pass

class AddressAdmin(object):
    pass

class OrderDetailAdmin(object):
    pass

class CommentAdmin(object):
    pass

class EatAdmin(object):
    pass

xadmin.site.register(YGUser,UserAdmin)
xadmin.site.register(YGEat,EatAdmin)
xadmin.site.register(YGOrder,OrderAdmin)
xadmin.site.register(YGOderDetail,OrderDetailAdmin)
xadmin.site.register(YGCart,CartAdmin)
xadmin.site.register(YGNav,NavAdmin)
xadmin.site.register(YGWheel,WheelAdmin)
xadmin.site.register(YGComment,CommentAdmin)
xadmin.site.register(YGAddress,AddressAdmin)
xadmin.site.register(YGNavDetail,NavDetailAdmin)
xadmin.site.register(YGGoods,GoodsAdmin)
xadmin.site.register(YGChosen,ChosenAdmin)

xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting)