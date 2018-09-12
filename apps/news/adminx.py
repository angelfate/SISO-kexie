__author__ = 'Nebula'
__date__ = '2018/6/18 21:26'
import xadmin

from .models import Organizations,Professions,Classrooms,Cadres,New

class OrganizationsAdmin(object):
    list_display = ['name','create_time']
    search_fields = ['name']
    list_filter = ['name','create_time']

class ProfessionsAdmin(object):
    list_display = ['name', 'create_time']
    search_fields = ['name',]
    list_filter = ['name', 'create_time']

class ClassroomsAdmin(object):
    list_display = ['name', 'create_time']
    search_fields = ['name',]
    list_filter = ['name', 'create_time']


class CadresAdmin(object):
    list_display = ['fullname','name','prof','classroom','buzhang','job','mobile','xuehao','create_time']
    search_fields = ['fullname','name','prof','classroom','buzhang','job','mobile','xuehao']
    list_filter = ['fullname','name','prof','classroom','buzhang','job','mobile','xuehao','create_time']


class NewAdmin(object):
    list_display = ['title','image', 'detil','content', 'create_time', 'modify_time','organization','students','boss','org','click_nums']
    search_fields =['title','image', 'detil', 'content', 'modify_time','organization','students','boss','org','click_nums']
    list_filter = ['title','image',  'detil','content', 'create_time', 'modify_time','organization','org','students','boss','click_nums']
    style_fields = {'content': 'ueditor'}



xadmin.site.register(Organizations,OrganizationsAdmin)
xadmin.site.register(Professions,ProfessionsAdmin)
xadmin.site.register(Classrooms,ClassroomsAdmin)
xadmin.site.register(Cadres,CadresAdmin)
xadmin.site.register(New,NewAdmin)