from datetime import datetime

from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
from DjangoUeditor.models import UEditorField
# Create your models here.


class Organizations(models.Model):
    """
    部门分类
    """
    name = models.CharField(verbose_name='部门组织', max_length=20)
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)   # 自动添加时间

    class Meta:
        verbose_name = '部门组织'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Professions(models.Model):
    """
    专业分类
    """
    name = models.CharField(verbose_name='专业', max_length=20)
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)  # 自动添加时间

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = verbose_name



class Classrooms(models.Model):
    """
    班级分类
    """
    name = models.CharField(verbose_name='班级', max_length=20)
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)  # 自动添加时间

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = verbose_name





class Cadres(models.Model):
    """
    部门干部
    """
    fullname = models.CharField(verbose_name='姓名', max_length=20) # 防止数据冲突，要加默认default
    name = models.CharField(verbose_name='年级',max_length=2)
    prof= models.ForeignKey(Professions,verbose_name='专业', max_length=20,on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classrooms,verbose_name='班级', max_length=20,on_delete=models.CASCADE)
    buzhang = models.ForeignKey(Organizations,verbose_name='所属部门', max_length=10,on_delete=models.CASCADE)
    job =  models.CharField(verbose_name='担任职务', max_length=20)
    xuehao = models.CharField(verbose_name="学号",max_length=9)
    mobile = models.CharField(verbose_name='手机号',max_length=11) # 长整型
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now)  # 字典添加时间

    class Meta:
        verbose_name = '部门干部'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class New(models.Model):
    """
    新闻
    """
    title = models.CharField(verbose_name='新闻标题', max_length=20)
    image = models.ImageField(upload_to="news/%Y%m", verbose_name=u"新闻Logo",default=u"image/default.jpg", max_length=100)
    # content = RichTextUploadingField(verbose_name='正文', default='')
    detil = models.CharField(verbose_name='新闻介绍', max_length=20,default=u"这是新闻介绍!")
    content = UEditorField(verbose_name=u'内容',default='',width=1000,height=300,imagePath='goods/images/',filePath='goods/files/')
    create_time = models.DateTimeField(verbose_name='创建时间',default=datetime.now) # 字典添加时间
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    organization = models.ForeignKey(Organizations,verbose_name="部门组织",on_delete=models.CASCADE)
    students = models.CharField(verbose_name="编辑人",max_length=10)
    boss = models.CharField(verbose_name="审核人",max_length=10)
    org = models.CharField(verbose_name="所属社团/院系等",max_length=10,default=u"科协")
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    index = models.IntegerField(verbose_name='1置顶0不置顶',default=0)

    class Meta:
        verbose_name = '新闻发布'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

