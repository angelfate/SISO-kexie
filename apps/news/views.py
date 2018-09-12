from django.shortcuts import render
from django.views.generic import View

from .models import New
from pure_pagination import PageNotAnInteger, Paginator
# Create your views here.

class NewView(View):
    """
    新闻页面首页
    """
    def get(self, request):
        # 填充数据(课程机构)
        all_news = New.objects.filter(index=0).order_by('-create_time')  # 查询所有index=0的新闻 [按照时间倒序]

        #置顶新闻
        top_news = New.objects.filter(index=1).order_by('-create_time')  # 查询所有 index=1 的数据 [按照时间倒序]

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_news, 15, request=request)
        all_new = p.page(page)

        return render(request, "news.html",{
            "all_news": all_news,
            "top_news": top_news,
            "all_new": all_new,  # 分页
        })


class NewContent(View):
    def get(self, request,id):
        # new_org = New.objects.get(id=int(new_id))  # 获取新闻id
        new_detail = New.objects.get(id=id)

        #每调用一次视图，点击数+1
        new_detail.click_nums+=1
        new_detail.save()
        return render(request, "news-content.html", {
            # "new_org": new_org,
            "new_detail": new_detail,
        })


#配置404 500错误页面
def page_not_found(request):
    return render(request, '404.html')


def page_errors(request):
    return render(request, '500.html')