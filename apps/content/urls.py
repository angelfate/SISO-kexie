__author__ = '未昔'
__date__ = '2018/8/21 11:23'

from django.conf.urls import url,include

from content.views import ContentView,AskForm


urlpatterns = [
    #联系我们页面
    url(r'^content/$', ContentView.as_view(), name="content"),  # 联系我们页面

    url(r'^add_ask/$', AskForm, name="add_ask"),  #用户咨询

]

