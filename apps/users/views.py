from django.shortcuts import render
from django.views.generic import View

from news.models import New
from .models import Logo,Banner
from cadres.models import Cadres
# Create your views here.

class NewView(View):
    """
    首页最新新闻
    """
    def get(self, request):
        # 填充数据()
        all_news = New.objects.all()  # 查询所有新闻
        # 最新新闻
        hot_news = all_news.order_by("-create_time")[:4]

        all_banners = Banner.objects.all()  # 获取所有轮播图
        # 最新的轮播图
        new_banners = all_banners.order_by("-index")[:4]

        #最新的三个干部
        new_cadres = Cadres.objects.all().order_by('-create_time')[:3]  # 查询最新的三个干部（倒序查询）

        return render(request, "index.html",{
            "all_news": all_news,
            "hot_news": hot_news,
            "new_banners": new_banners,
            "new_cadres": new_cadres,
        })




