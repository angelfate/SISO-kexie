"""KeXie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.views.generic import TemplateView # 这里处理的文件是静态文件（这是一个类，调用类里面的这个方法）
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView # 这里处理的文件是静态文件（这是一个类，调用类里面的这个方法）

from users import views
import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

from KeXie.settings import STATIC_ROOT
from KeXie.settings import MEDIA_ROOT

urlpatterns = [
    url(r'xadmin/', xadmin.site.urls),
    url(r'^$', views.NewView.as_view(), name="index"),  # as_view 把 Template 转换成 view

    # 新闻url配置
    url(r'^news/', include(('news.urls', "news"), namespace="news")),
    # 联系我们页面url配置
    url(r'^content/', include(('content.urls', "content"), namespace="content")),
    # 关于我们页面url配置
    url(r'^about/', include(('about.urls', "about"), namespace="about")),
    # 历届干部url配置
    url(r'^cadres/', include(('cadres.urls', "cadres"), namespace="cadres")),
    # 活动页面url配置
    url(r'^activities/', include(('activities.urls', "activities"), namespace="activities")),


    # 富文本编辑器
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    #添加静态文件的访问处理函数
    url(r'^static/(?P<path>.*)/$', serve, {'document_root': STATIC_ROOT}),

    # # 配置上传文件的访问处理函数
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')), # 取出路径，放到path下面，（.*：取出全部,document_root:去哪个路径下面寻找）

    #配置上传的静态文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 取出路径，放到path下面，（.*：取出全部,document_root:去哪个路径下面寻找）

    #静态文件
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)



# 配置全局404页面
hander404 = 'page_not_found'

# 配置全局505页面
hander505 = 'page_errors'