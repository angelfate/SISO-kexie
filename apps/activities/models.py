from datetime import datetime

from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
from DjangoUeditor.models import UEditorField
# Create your models here.


class ActBanner(models.Model):  # 活动页轮播图
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="activities/banner/%Y/%m/%d",verbose_name=u"轮播图",max_length=100,default="image/default.jpg")
    url = models.URLField(max_length=500,verbose_name=u"访问地址")  # 跳转链接
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name


class Range(models.Model):
    """
    招募对象
    """
    name = models.CharField(max_length=20,verbose_name=u"招募范围")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '部门组织'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Act(models.Model):
    """
       活动状态
       """
    name = models.CharField(max_length=20, verbose_name=u"活动状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '活动状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Cadres(models.Model):
    """
    活动内容
    """
    name = models.CharField(verbose_name='活动名',max_length=20)
    image = models.ImageField(upload_to="activities/logo/%Y/%m/%d", verbose_name=u"活动Logo", default=u"image/default.jpg",
                              max_length=100)
    detil = models.CharField(verbose_name='活动介绍', max_length=20, default=u"未填写")
    content = UEditorField(verbose_name=u'活动内容', default='', width=1000, height=300, imagePath='activities/images/',
                           filePath='activities/files/')
    ran = models.ForeignKey(Range,verbose_name='招募对象', max_length=20,on_delete=models.CASCADE)
    students = models.IntegerField(verbose_name="招募人数")
    place = models.CharField(verbose_name="活动地点", max_length=20)
    star_time = models.DateTimeField(verbose_name="开始时间",default=datetime.now)
    end_time = models.DateTimeField(verbose_name="截止时间", default=datetime.now)
    act = models.ForeignKey(Act,verbose_name="活动状态", max_length=20,on_delete=models.CASCADE)
    click_nums = models.IntegerField(verbose_name='浏览量', default=99)
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)

    class Meta:
        verbose_name = '活动内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    """
    赞助商
    """
    name = models.CharField(verbose_name='赞助商名', max_length=20)
    logo = models.ImageField(upload_to="activities/sponsor/%Y/%m/%d", verbose_name=u"赞助商logo", max_length=100,
                              default="image/default.jpg")
    detil = models.CharField(verbose_name='赞助商简介', max_length=20, default=u"未填写")
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = '赞助商名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

