__author__ = '未昔'
__date__ = '2018/8/21 11:40'
import xadmin

from .models import UserAsk


class UserAskAdmin(object):
    list_display = ['name', 'email','mobile','zy','msg','add_time']
    search_fields = ['name', 'email','mobile','zy','msg','add_time']
    list_filter = ['name', 'email','mobile','zy','msg','add_time']


xadmin.site.register(UserAsk,UserAskAdmin)
