from datetime import datetime

from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
from news.models import Professions
# Create your models here.


class Cadres(models.Model):
    """
       历届干部
    """
    name = models.CharField(verbose_name='名字', max_length=20)
    image = models.ImageField(upload_to="cardes/%Y%m", verbose_name=u"头像",default=u"image/default.jpg",max_length=100)
    grade = models.IntegerField(verbose_name='年级')
    job = models.CharField(verbose_name='担任职务', max_length=20)
    professions = models.CharField(verbose_name='专业', max_length=20,default=u"计算机信息管理")
    declaration = models.CharField(verbose_name="个人宣言",max_length=20)
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)  # 自动添加时间

    class Meta:
        verbose_name = '历届干部'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  '{0}'.format("历届干部")



