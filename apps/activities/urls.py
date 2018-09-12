__author__ = '未昔'
__date__ = '2018/8/31 21:11'


from django.conf.urls import url,include
from .views import ActView,ActdetialView
# from organization.views import OrgView,AddUserAskView,OrgHomeView,OrgCourseView


urlpatterns = [
    #活动页面
    url(r'^act_list/$', ActView.as_view(), name="act_list"),  # 新闻页面
    url(r'^act_detial/(\d+)$', ActdetialView.as_view(), name="act_detial"),  # (?P<org_id>\d+) 那个页面：取出数字
]
