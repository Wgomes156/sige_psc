"""
Django PRODUCTION settings for sige_psc project.
Configuração para VPS HostGator — domínio pscservice.site

Uso: export DJANGO_SETTINGS_MODULE=sige_psc.settings_prod
"""
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(find_dotenv(), override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ───────────────────────── SEGURANÇA ─────────────────────────

SECRET_KEY = os.environ["SECRET_KEY"]

# PRODUÇÃO: Debug desligado
DEBUG = False

ALLOWED_HOSTS = [
    "pscservice.site",
    "www.pscservice.site",
]

CSRF_TRUSTED_ORIGINS = [
    "https://pscservice.site",
    "https://www.pscservice.site",
]


# ───────────────────────── APPS ─────────────────────────

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Servir static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ───────────────────────── URLS & TEMPLATES ─────────────────────────

ROOT_URLCONF = 'sige_psc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
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

WSGI_APPLICATION = 'sige_psc.wsgi.application'


# ───────────────────────── BANCO DE DADOS ─────────────────────────

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASS"],
        'HOST': os.environ["DB_HOST"],
        'PORT': os.environ["DB_PORT"],
    }
}


# ───────────────────────── AUTENTICAÇÃO ─────────────────────────

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_URL = "/login"
LOGOUT_REDIRECT_URL = '/'
AUTH_USER_MODEL = "website.User"


# ───────────────────────── INTERNACIONALIZAÇÃO ─────────────────────────

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')

APPEND_SLASH = True


# ───────────────────────── STATIC FILES ─────────────────────────

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ───────────────────────── EMAIL ─────────────────────────

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS = os.environ["EMAIL_USE_TLS"]
EMAIL_PORT = os.environ["EMAIL_PORT"]
EMAIL_HOST = os.environ["EMAIL_HOST"]


# ───────────────────────── SEGURANÇA HTTPS ─────────────────────────

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 ano
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# ───────────────────────── DEFAULT ─────────────────────────

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
