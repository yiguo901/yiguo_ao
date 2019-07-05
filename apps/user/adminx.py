from django.contrib import admin

# Register your models here.
import xadmin
from goods.models import YGGoods
#from user.models import *
from user.models import YGUser


class UserAdmin(object):
    list_display = ['id','u_phone','nickname','u_level',
                    'gender','idcard','img']
    search_fields = ['nickname','gender']
    list_filter = ['nickname','u_level','gender']
    ordering = ('id',)
    list_per_page = 30
    model_icon = 'fa fa-check-square'

xadmin.site.register(YGUser,UserAdmin)

