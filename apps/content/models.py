from datetime import datetime

from django.db import models

# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    email = models.EmailField(max_length=30, verbose_name=u"邮箱")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    zy = models.CharField(max_length=20, verbose_name=u"专业")
    msg = models.TextField(max_length=300, verbose_name=u"资讯信息")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name

