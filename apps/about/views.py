from django.shortcuts import render
from django.views.generic import View

from .models import Whos,History,Servers
from pure_pagination import PageNotAnInteger, Paginator
# Create your views here.

class AboutView(View):
    def get(self, request):
        all_whos =  Whos.objects.all() # 查询所有的 who（我们是谁）
        new_whos = all_whos.order_by("-name")[:2] # 倒叙取出2条信息

        all_histories = History.objects.all()
        new_histories = all_histories.order_by("-name")[:5]  # 倒叙取出2条信息

        all_servers = Servers.objects.all()
        new_servers = all_servers.order_by("-name")[:8]

        return render(request, "about.html", {
            "all_whos": all_whos,
            "new_whos": new_whos,
            "all_histories": all_histories,
            "new_histories": new_histories,
            "all_servers": all_servers,
            "new_servers": new_servers,
        })