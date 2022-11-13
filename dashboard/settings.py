"""
Django settings for dashboard project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from os import environ

# load .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q6t0wypa(c)h23%(%u%nb*#x4(69(g(s=b@@t_1shp@k(c&v%v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = environ['SERVERNAMES'].split(' ')

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'rest_framework.authtoken',
	'dashboard',
	'api',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dashboard.urls'

TEMPLATES = [
	{
	'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'DIRS': [
	BASE_DIR/'templates',
	BASE_DIR/'dashboard'/'templates',
	],
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

WSGI_APPLICATION = 'dashboard.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
	# SQLite3
	# 'default': {
	#     'ENGINE': 'django.db.backends.sqlite3',
	#     'NAME': BASE_DIR / 'db.sqlite3',
	# }

	# PostgreSQL
	'default': {
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
	'HOST': environ['DB_HOST'],
	'PORT': environ['DB_PORT'],
	'NAME': environ['DB_NAME'],
	'USER': environ['DB_USER'],
	'PASSWORD': environ['DB_PWD'],
	}
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'api.User'

REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': [
	# 'rest_framework.permissions.IsAuthenticated',
	],
	'DEFAULT_AUTHENTICATION_CLASSES': [
	# 'rest_framework.authentication.TokenAuthentication',
	],
}
LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TIME_ZONE = 'Asia/Seoul'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'dashboard', 'staticfiles'),)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

APPEND_SLASH = True