from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):  # 继承原有的 user 表
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default="male")
    address = models.CharField(max_length=100,default=u"")
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):  # __unicode__ on Python 2
        return self.username


class EmailVerifyRecord(models.Model):  # 邮箱验证码
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register",u"注册"),("forget",u"找回密码")),max_length=10,verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):  # __unicode__ on Python 2
        return '{0}({1})'.format(self.code, self.email)

class Banner(models.Model):  # 首页轮播图
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y%m",verbose_name=u"轮播图",max_length=100)
    url = models.URLField(max_length=500,verbose_name=u"访问地址")  # 跳转链接
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

class Logo(models.Model):  # 首页轮播图
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="logo/%Y%m",verbose_name=u"LOGO",max_length=100,default=u"image/default.png")
    url = models.URLField(max_length=500,verbose_name=u"访问地址",default="http://127.0.0.1:1234/")  # 跳转链接
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"Logo"
        verbose_name_plural = verbose_name


