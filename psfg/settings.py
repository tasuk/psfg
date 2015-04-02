"""
Django settings for psfg project.

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
# SECRET_KEY = 'intentionally commented out'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = [
    '.peopleskillsforgeeks.com',
]


# Application definition

INSTALLED_APPS = (
    # cms
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'djangocms_admin_style',
    'djangocms_text_ckeditor',

    # django defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'psfg',
    'content',
    'feedback',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware', // ehh, security...
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'psfg.urls'
WSGI_APPLICATION = 'psfg.wsgi.application'
SITE_ID = 1


# Templates

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

CMS_TEMPLATES = (
    ('content/home.html', 'Homepage'),
    ('content/articlelist.html', 'Article List'),
    ('content/article.html', 'Article'),
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGES = [ ('en', 'English') ]
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# CKEditor

CKEDITOR_SETTINGS = {
    'allowedContent': 'p;a[!href];em;strong;h2;h3;h4;ul;ol;li;hr;pre;img[!src];table;tr;th;td',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Format'],
        ['PasteText'],
        ['Bold', 'Italic', '-', 'RemoveFormat'],
        ['Link', 'Unlink'],
        ['NumberedList', 'BulletedList', 'Table'],
        ['Maximize'],
        ['Source'],
    ],
}

try:
    from .local_settings import *
except ImportError as e:
    pass
