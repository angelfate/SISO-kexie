__author__ = 'Nebula'
__date__ = '2018/8/17 12:24'
import xadmin
from xadmin import views

from .models import EmailVerifyRecord,Banner,Logo


class BaseSetting(object): # 主题 更改
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):  # title和 footer
    site_title = "SISO科协后台管理系统"
    site_footer = "SISO科学技术协会"
    menu_style = "accordion"  # 可以收起 App


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time'] # 重载
    search_fields = ['code', 'email', 'send_type']  # 查
    list_filter = ['code', 'email', 'send_type', 'send_time'] # 时间筛选功能
    model_icon = 'fa fa-address-book-o'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']



class LogoAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']



xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin) # xadmin.site.register 注册一下
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Logo,LogoAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting) # 主题 注册
xadmin.site.register(views.CommAdminView, GlobalSettings) # 标题和 底端字体 的 注册
