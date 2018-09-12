from django.shortcuts import render
from django.views.generic import View

from .models import Cadres
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class CadresView(View):
    """
    历届干部页面首页
    """
    def get(self, request):
        # 填充数据(历届干部)
        all_cadres = Cadres.objects.all().order_by('-create_time')   # 查询所有干部

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_cadres,2,request=request)
        all_cadre = p.page(page)

        return render(request, "cadres.html",{
            "all_cadres": all_cadre,# 分页
        })
