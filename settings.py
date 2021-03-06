"""
Django settings for KeXie project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))   # 添加APP路径，让项目搜索到
sys.path.insert(0,os.path.join(BASE_DIR,'extra_app'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's2voqbrw%5g#v)6de$jctlu6i2zlv6rn%ubm&g7*_th7z4r4ne'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'users',  # 用户app
    'activities',# 活动发布app
    'cadres',# 干部app
    'news',# 新闻发布app
    'content',# 联系我们app
    'about',#关于我们app
    'haystack',
    # 'ckeditor',  # 富文本
    # 'ckeditor_uploader', # 富文本上传路径
    'DjangoUeditor',  # 富文本
    'xadmin', # 后台管理系统xadmin
    'crispy_forms', # xadmin依赖
    'reversion',# xadmin依赖
    'captcha',
    'pure_pagination', # 分页
]

AUTH_USER_MODEL = 'users.UserProfile'    # 重载一个settings.py 的方法

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'KeXie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'KeXie.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '',
        'NAME': 'kexie',
        'PORT': '3306',
        'CONN_MAX_AGE': 5000,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#
# STATIC_URL = '/static/'
# # STATICFILES_DIRS = (
# #     os.path.join(BASE_DIR, 'static'),
# # )
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#静态文件路径
STATIC_URL = '/static/'
STATIC_ROOT = 'static'


# media_confige 静态文件上传
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

PAGINATION_SETTINGS = {  # 分页设置
    'PAGE_RANGE_DISPLAYED': 3,  # PAGE_RANGE_DISPLAYED是将显示的当前页面的邻近页面数量（默认值为10）
    'MARGIN_PAGES_DISPLAYED': 3, # MARGIN_PAGES_DISPLAYED是将显示的第一页和最后一页相邻的页数（默认值为2）

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

#搜索
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'KeXie.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

UEDITOR_SETTINGS = {
                       "toolbars": {  # 定义多个工具栏显示的按钮，允行定义多个
                           "name1": [['source', '|', 'bold', 'italic', 'underline']],
                           "name2": []
                   },
                   "images_upload":{
                                       "allow_type": "jpg,png",  # 定义允许的上传的图片类型
                                       "max_size": "2222kb"  # 定义允许上传的图片大小，0代表不限制
                                   },
                                   "files_upload": {
    "allow_type": "zip,rar",  # 定义允许的上传的文件类型
    "max_size": "2222kb"  # 定义允许上传的文件大小，0代表不限制
},
"image_manager": {
    "location": ""  # 图片管理器的位置,如果没有指定，默认跟图片路径上传一样
},
}

# # ckeditor config
# #在settings.py文件中写入cdeditor的配置
# CKEDITOR_UPLOAD_PATH = 'article_files/'
# CKEDITOR_JQUERY_URL ='js/jquery-3.2.1.min.js'
# CKEDITOR_IMAGE_BACKEND = 'pillow'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'language': 'zh-cn',
#         'toolbar_YourCustomToolbarConfig': [
#
#             {'name': 'clipboard', 'items': ['Undo', 'Redo', '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord']},
#             {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']},
#             {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'Smiley']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'editing', 'items': ['Find', 'Replace', '-']},
#             {'name': 'tools', 'items': ['Maximize']},
#             '/',
#             {'name': 'styles', 'items': ['Format', 'Font', 'FontSize']},
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'paragraph',
#              'items': ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
#             {'name': 'document', 'items': ['Source']},
#         ],
#         'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
#         'width': '100%',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage',  # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#     }
# }
# CKEDITOR_ALLOW_NONIMAGE_FILES = False
# CKEDITOR_BROWSE_SHOW_DIRS = True
