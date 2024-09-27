"""
Django settings for Mozio task project.
"""
import os
import environ  # type: ignore
import sys
from dotenv import load_dotenv  # type: ignore
from pathlib import Path

# Set the project base directory
BASE_DIR = Path(__file__).resolve().parent

ENV = os.environ.get('ENV', default='dev')
# Take environment variables from .env file
load_dotenv(f'.env.{ENV}')

# Application definition
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.gis",
    "django_extensions",
    'django_filters',
    'mozio.apps.MozioConfig',
    'rest_framework',
    'corsheaders',
    'rest_framework_gis',
    'drf_yasg',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': os.environ.get('DATABASE_NAME'),
         'USER': os.environ.get('DATABASE_USER'),
         'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
         'HOST': os.environ.get('DATABASE_HOST'),
         'PORT': os.environ.get('POSTGRES_PORT')
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'EXCEPTION_HANDLER': 'mozio.error_handling.custom_exception_handler',
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'USE_SESSION_AUTH': False
}

ALLOWED_HOSTS = ["*", "mozio.tester.ninja", "54.173.189.237", "*"]
CORS_ALLOWED_ORIGINS = ["https://mozio.tester.ninja", "http://54.173.189.237", "http://*"]

CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', default="")
SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', default=False)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', default='#um2g($a1-#2d(enmn!3pmg6axus*wbip_y#p!ezs0*$)(^!^o')
ENV_ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
DEBUG = os.environ.get('DEBUG', default='True')


GDAL_LIBRARY_PATH = os.environ.get("GDAL_LIBRARY_PATH")
GEOS_LIBRARY_PATH = os.environ.get("GEOS_LIBRARY_PATH")
PROJ_LIBRARY_PATH = os.environ.get("PROJ_LIBRARY_PATH")

