__author__ = '未昔'
__date__ = '2018/8/31 19:41'
import xadmin

from .models import ActBanner,Range,Act,Cadres,Sponsor

class ActBannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']


class RangeAdmin(object):
    list_display = ['name','add_time']
    search_fields = ['name']
    list_filter = ['name','add_time']


class Actdmin(object):
    list_display = ['name','add_time']
    search_fields = ['name']
    list_filter = ['name','add_time']


class CadresAdmin(object):
    list_display = ['name','image','detil','content','ran','students','place','star_time','end_time','act','create_time']
    search_fields = ['name','image','detil','content','ran','students','place','star_time','end_time','act']
    list_filter = ['name','image','detil','content','ran','students','place','star_time','end_time','act','create_time']
    style_fields = {'content': 'ueditor'}


class SponsorAdmin(object):
    list_display = ['name','logo','detil','create_time']
    search_fields = ['name','logo','detil']
    list_filter = ['name','logo','detil','create_time']


xadmin.site.register(ActBanner,ActBannerAdmin)
xadmin.site.register(Range,RangeAdmin)
xadmin.site.register(Act,Actdmin)
xadmin.site.register(Cadres,CadresAdmin)
xadmin.site.register(Sponsor,SponsorAdmin)



