__author__ = '未昔'
__date__ = '2018/8/20 13:02'

from django.conf.urls import url,include
from news.views import NewView,NewContent
# from organization.views import OrgView,AddUserAskView,OrgHomeView,OrgCourseView


urlpatterns = [
    #课程机构首页
    url(r'^list/$', NewView.as_view(), name="new_list"),  # 新闻页面
    url(r'^new_content/(\d+)$', NewContent.as_view(), name="new_content"),  # (?P<org_id>\d+) 那个页面：取出数字
    # url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),  # (?P<org_id>\d+) 那个页面：取出数字
    # url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),  # 机构课程列表页url
]

