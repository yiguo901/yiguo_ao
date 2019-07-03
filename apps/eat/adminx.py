from django.contrib import admin

# Register your models here.
import xadmin
from eat.models import YGEat


class EatAdmin(object):
    list_display = ['id', 'eat_img', 'eat_content','eat_time']
    list_filter = ['id', 'eat_time']
    search_field = ['id','eat_time']
    ordering = ('id',)
    list_action_page = 30
    model_icon = 'fa fa-check-square'


xadmin.site.register(YGEat,EatAdmin)