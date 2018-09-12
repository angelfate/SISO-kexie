__author__ = '未昔'
__date__ = '2018/8/21 16:08'

from django.conf.urls import url,include
from .views import AboutView
# from organization.views import OrgView,AddUserAskView,OrgHomeView,OrgCourseView


urlpatterns = [
    #关于我们首页
    url(r'^about/$', AboutView.as_view(), name="about"),  # 关于我们页面
]


