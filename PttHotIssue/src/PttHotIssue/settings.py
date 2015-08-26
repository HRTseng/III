# -*- coding:utf-8 -*-
"""
Django settings for PttHotIssue project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9(_l#aj22oh7o7c_y-17mw2d&x-f=8_qyj+&+wrq%758#u3mh7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


#樣板位置
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'), #BASE_DIR + "/templates/"
   
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
    'corsheaders', # CORS
    
    'HotIssue', #置入 HotIssue 應用
    'WebApi',
    
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
        'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'PttHotIssue.urls'

WSGI_APPLICATION = 'PttHotIssue.wsgi.application'


CORS_ORIGIN_ALLOW_ALL = False 
CORS_ALLOW_CREDENTIALS = True 
CORS_ORIGIN_WHITELIST = (     'http://localhost:8000' ,
                              'http://10.120.30.5:8000' ,
                               )


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
#     'pttData':{
#         'ENGINE'    :   'django.db.backends.mysql',
#         'NAME'      :   'ptt',              #Database
#         'USER'      :   'zb101',            #登入帳號
#         'PASSWORD'  :   'zb101',            #登入密碼
#         'HOST'      :   '10.120.30.5',      #IP
#         'PORT'      :   '3306',             #Port
# 
#     }       
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-TW'#中文-台灣

TIME_ZONE = 'Asia/Taipei' #亞洲/台北

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
