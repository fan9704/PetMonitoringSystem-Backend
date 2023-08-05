"""
Django settings for PetMonitoringSystemBackend project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import json
import os
import sys
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import logstash

load_dotenv(find_dotenv())
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '123456')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', True)

ALLOWED_HOSTS = ["127.0.0.1", "*"]
# CORS Settings
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]
CORS_ALLOWED_HEADERS = "*"
CORS_ORIGIN_ALLOW_METHODS = "*"
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_seed',
    'corsheaders',
    'django_redis',
    'drf_yasg',
    'channels',

    # 'django_forest',
    # 'django_prometheus',

    'health_check',  # required
    'health_check.db',  # stock Django health checkers
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.migrations',
    # 'health_check.contrib.rabbitmq',  # requires RabbitMQ broker
    'health_check.contrib.redis',  # requires Redis

    'api',
    'ws',
]
if os.getenv("ELASTICSEARCH_ENABLE", False):
    INSTALLED_APPS += ['django_elasticsearch_dsl', ]

MIDDLEWARE = [
    # 'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_prometheus.middleware.PrometheusAfterMiddleware'
]

ROOT_URLCONF = 'PetMonitoringSystemBackend.urls'

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

WSGI_APPLICATION = 'PetMonitoringSystemBackend.wsgi.application'
ASGI_APPLICATION = 'PetMonitoringSystemBackend.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [f"redis://{os.getenv('REDIS_HOST', '127.0.0.1')}:{os.getenv('REDIS_PORT', 6379)}/2"],
        },
    },
    "memory": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
}
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB", "PET"),
        'USER': os.getenv("POSTGRES_USER", "test"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "123456"),
        'HOST': os.getenv("POSTGRES_DB_URL", "127.0.0.1"),
        'PORT': '5432'
    },
    'test': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_TEST_DB", "TEST"),
        'USER': os.getenv("POSTGRES_USER", "test"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "123456"),
        'HOST': os.getenv("POSTGRES_DB_URL", "127.0.0.1"),
        'PORT': '5432'
    },
}
if 'test' in sys.argv:
    DATABASES['default'] = DATABASES['test']
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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'zh-TW'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEFAULT_CHARSET = 'utf-8'  # 'latin-1'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Elasticsearch DSL Configuration
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': os.getenv("ELASTICSEARCH_ENDPOINT", "127.0.0.1:9200")
    },
}

# RabbitMQ Config
RABBITMQ_CONFIG = {
    "enable": os.getenv("RABBITMQ_ENABLE", False),
    "username": os.getenv("RABBITMQ_USERNAME", "guest"),
    "password": os.getenv("RABBITMQ_PASSWORD", "guest"),
    "serverip": os.getenv("RABBITMQ_SERVER_IP", "127.0.0.1"),
    "port": os.getenv("RABBITMQ_PORT", "1883"),
    "vhost": os.getenv("RABBITMQ_VIRTUAL_HOST", "/")
}
BROKER_URL = f'amqp://{RABBITMQ_CONFIG["username"]}:{RABBITMQ_CONFIG["password"]}@{RABBITMQ_CONFIG["serverip"]}:{RABBITMQ_CONFIG["port"]}{RABBITMQ_CONFIG["vhost"]}'

# chatBot Config
CHATGPT_CONFIG = {
    "enable": os.getenv("CHATGPT_ENABLE", False),
    "api_key": os.getenv("CHATGPT_APIKEY", None)
}

# Redis Cache

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{os.getenv('REDIS_HOST', '127.0.0.1')}:{os.getenv('REDIS_PORT', ':6379')}/1",
        # 1 is Database Number
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        'KEY_PREFIX': 'Cache'
    },
}
REDIS_URL = CACHES["default"]["LOCATION"]

# Django Forest admin Setting
# FOREST = {
#     'FOREST_URL': os.getenv("FOREST_URL", 'https://api.forestadmin.com'),
#     'FOREST_ENV_SECRET': os.getenv("FOREST_ENV_SECRET", None),
#     'FOREST_AUTH_SECRET': os.getenv("FOREST_AUTH_SECRET", None)
# }
APPEND_SLASH = False

# Logstash Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'logstash': {
            'level': 'DEBUG',
            'class': 'logstash.TCPLogstashHandler',
            'host': os.getenv("LOGSTASH_SERVER_IP", 'localhost'),
            'port': os.getenv("LOGSTASH_PORT", 5000),  # Default value: 5959
            'version': 1,
            # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
            'message_type': 'django',  # 'type' field in logstash message. Default value: 'logstash'.
            'fqdn': False,  # Fully qualified domain name. Default value: false.
            'tags': ['django.request'],  # list of tags. Default: None.
        }
    },
    'root': {
        'handlers': ['console', 'logstash'],
        'level': 'DEBUG',
    },
}

# JWT
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    )

}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
# Firebase Configuration
FIREBASE_ENABLE = os.getenv("FIREBASE_ENABLE", False)
FIREBASE_CONFIG: dict = dict({
    "type": "service_account",
    "project_id": "petmonitoringsystem-729da",
    "private_key_id": "e6dd9c92522e7452207399be3a6d09d879caa254",
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY", None).replace('\\n', '\n'),
    "client_email": "firebase-adminsdk-85ae8@petmonitoringsystem-729da.iam.gserviceaccount.com",
    "client_id": "101784752751681660495",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-85ae8%40petmonitoringsystem-729da.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})
# Actual directory user files go to
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
