from datetime import datetime

from django.db import models
# Create your models here.

class Whos(models.Model):
    """
    我们是谁分类
    """
    name = models.CharField(verbose_name='我们是谁', max_length=100)
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)   # 自动添加时间

    class Meta:
        verbose_name = '我们是谁'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class History(models.Model):
    """
    我们的历史分类
    """
    name = models.CharField(verbose_name='我们的历史', max_length=100)
    time = models.IntegerField(verbose_name=u"年份")
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)   # 自动添加时间

    class Meta:
        verbose_name = '我们的历史'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Servers(models.Model):
    """
    我们的历史分类
    """
    name = models.CharField(verbose_name='我们的服务', max_length=20)
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)   # 自动添加时间

    class Meta:
        verbose_name = '我们的服务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
