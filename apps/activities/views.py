from django.shortcuts import render
from django.views.generic import View

from .models import Cadres,Sponsor
from pure_pagination import PageNotAnInteger, Paginator
# Create your views here.

class ActView(View):
    """
    活动页面首页
    """
    def get(self, request):
        # 填充数据()
        all_acts = Cadres.objects.all()  # 查询所有活动
        # 最新新闻
        new_acts = all_acts.order_by("-create_time")[:3]

        #赞助商
        all_sponsors = Sponsor.objects.all()  # 查询所有赞助商
        #最新赞助商
        new_sponsors  = all_sponsors.order_by("-create_time")[:3]

        # # 分页
        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1
        #
        # p = Paginator(all_news, 15, request=request)
        # all_new = p.page(page)

        return render(request, "activities.html", {
            "all_acts": all_acts,
            "new_acts": new_acts,
            "new_sponsors": new_sponsors,
        })


class ActdetialView(View):
    """
    活动详情页
    """
    def get(self, request,id):
        all_acts = Cadres.objects.get(id=id)  # 查询所有活动
        # 每调用一次视图，点击数+1
        all_acts.click_nums += 1
        all_acts.save()

        return render(request, "activities-content.html", {
            "act": all_acts,
        })
