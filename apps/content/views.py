from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

from .forms import UserAskForm
from  .models import UserAsk

# Create your views here.

class ContentView(View):
    def get(self, request):
        return render(request, "contact.html")


def AskForm(request):
    if request.method == "POST":
        send_form = UserAskForm(request.POST)  # 实例化 \ 初始化form
        if send_form.is_valid():  # 验证是否合法（即是否满足forms.py的设置）
            msg = request.POST.get("msg", "")  # 取出 user_name 和 pass_word
            name = request.POST.get("name", "")
            if UserAsk.objects.filter(msg=msg,name=name):  # 判断 用户是否存在（如果存在）
                return render(request, "contact.html", {"register_form": send_form,
                                                         "msg": "请勿重复提交!"})  # 即 这个 email已经被注册过，不存在就进行下面的操作,传回form回填信息，天使吧验证码保存
            name = request.POST.get("name", "")  # 取出 user_name
            email =  request.POST.get("email", "")
            mobile =  request.POST.get("mobile", "")
            zy =  request.POST.get("zy", "")
            msg =  request.POST.get("msg", "")
            content = authenticate(name=name,email=email,mobile=mobile,zy=zy,msg=msg)

            user_ask = UserAsk()
            user_ask.name = name
            user_ask.mobile = mobile
            user_ask.email = email
            user_ask.zy = zy
            user_ask.msg = msg
            user_ask.save()

            if content is not None:
                login(request,content)
                return render(request,"contact.html")
            else:
                return render(request,"contact.html",{"msg":"添加信息出错"})
    elif request.method =="GET":
        return render(request,"contact.html")




