__author__ = '未昔'
__date__ = '2018/8/22 16:12'

import xadmin

from .models import Cadres

class CadresAdmin(object):
    list_display = ['name','image','grade','job','declaration','professions','create_time']
    search_fields = ['name','image','grade','job','declaration','professions']
    list_filter = ['name','image','grade','job','declaration','professions','create_time']


xadmin.site.register(Cadres,CadresAdmin)
