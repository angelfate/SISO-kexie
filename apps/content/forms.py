__author__ = 'Nebula'
__date__ = '2018/6/27 15:47'
import re
from django import forms

from content.models import UserAsk


class UserAskForm(forms.ModelForm):
    msg = forms.CharField(required=True) # 验证msg (是否符合正则表达式)

    class Meta:
        model = UserAsk
        fields = ['name','email','mobile', 'zy','msg']


    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']  # 取出form的mobile
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):   # mobile 是否满足正则表达式 （clean 对每一个字段进行了自定义封装  ）
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")