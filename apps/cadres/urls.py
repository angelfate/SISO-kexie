__author__ = '未昔'
__date__ = '2018/8/22 16:12'

from django.conf.urls import url,include
from .views import CadresView
# from organization.views import OrgView,AddUserAskView,OrgHomeView,OrgCourseView


urlpatterns = [
    #历届干部
    url(r'^list/$', CadresView.as_view(), name="cadres_list"),  # 历届干部页面
]

