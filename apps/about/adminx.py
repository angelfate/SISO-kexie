__author__ = '未昔'
__date__ = '2018/8/21 16:09'

import xadmin

from .models import Whos,History,Servers


class WhosAdmin(object):
    list_display = ['name','create_time']
    search_fields = ['name']
    list_filter = ['name','create_time']

class HistoryAdmin(object):
    list_display = ['name','time','create_time']
    search_fields = ['name',]
    list_filter = ['name','time', 'create_time']

class ServersAdmin(object):
    list_display = ['name', 'create_time']
    search_fields = ['name',]
    list_filter = ['name', 'create_time']



xadmin.site.register(Whos,WhosAdmin)
xadmin.site.register(History,HistoryAdmin)
xadmin.site.register(Servers,ServersAdmin)

