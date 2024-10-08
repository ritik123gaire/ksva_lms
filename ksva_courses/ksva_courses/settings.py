"""
Django settings for ksva_courses project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-atzgn&xf2&s0wuzucge7_ny3o$9c5ce@_q2%^b_otm13n&za6c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'course',
    
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

ROOT_URLCONF = 'ksva_courses.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ksva_courses.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Directory where static files will be collected
STATIC_URL = '/static/'

# The directory where static files are collected to during `collectstatic`
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Directories to look for static files during development
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

JAZZMIN_SETTINGS = {
    "site_title": "KSVA Course",  # Customize this as needed
    "site_header": "Your Admin Header",  # Customize this as needed
    "site_brand": "KSVA Course",  # Customize this as needed
    # "site_logo": "path/to/your/logo.png",  # Update this to your logo path
    # "site_icon": "path/to/your/icon.png",  # Optional: update to your favicon path
    "welcome_sign": "Welcome to the Admin Dashboard",  # Customize this as needed
    "copyright": "KSVA Tech Solutions",  # Customize this as needed

    "navigation_expanded": True,  # Expand the sidebar by default
    "show_ui_builder": False,  # Disable UI builder feature if not needed
    "hide_apps": [],  # List of apps to hide
    "hide_models": [],  # List of models to hide
    "order_with_respect_to": ['auth', 'contenttypes', 'sessions'],  # Order of apps in the sidebar

    # # Customize the look and feel of the admin interface
    # "custom_css": "path/to/your/custom.css",  # Path to custom CSS file
    # "custom_js": "path/to/your/custom.js",  # Path to custom JavaScript file

     "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "course": "fas fa-school",
        "course.course": "fas fa-book",
        "course.studentinfo": "fas fa-user-graduate",
        "course.instructor": "fas fa-chalkboard-teacher",
        "course.category": "fas fa-list-alt",  
    },

    

}

