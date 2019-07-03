from django.contrib import admin

# Register your models here.
import xadmin
from home.models import *

class WheelAdmin(object):
    list_display = ['img', 'name']
    list_filter = ['name']
    search_field = ['name']
    ordering = ('id',)
    list_wheel_page = 30
    model_icon = 'fa fa-check-square'

class ChosenAdmin(object):
    list_display = ['img', 'name']
    list_filter = ['name']
    search_field = ['name']
    ordering = ('id',)
    list_addr_page = 30
    model_icon = 'fa fa-check-square'

class NavAdmin(object):
    list_display = ['img', 'name']
    list_filter = ['name']
    search_field = ['name']
    ordering = ('id',)
    list_addr_page = 30
    model_icon = 'fa fa-check-square'

class NavDetailAdmin(object):
    list_display = ['img', 'img']
    list_filter = ['img']
    search_field = ['img']
    ordering = ('id',)
    list_addr_page = 10
    model_icon = 'fa fa-check-square'


xadmin.site.register(YGNav,NavAdmin)
xadmin.site.register(YGWheel,WheelAdmin)
# xadmin.site.register(YGComment,CommentAdmin)
# xadmin.site.register(YGAddress,AddressAdmin)
xadmin.site.register(YGNavDetail,NavDetailAdmin)
xadmin.site.register(YGChosen,ChosenAdmin)