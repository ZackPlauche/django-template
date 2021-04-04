import os
import django_heroku
import dj_database_url
import dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Local Environment Variable Initialization
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    # 'yourhost.com',
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
]

# Application definition

INSTALLED_APPS = [
    'base',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

OPTIONAL_APPS = [
    'adminsortable2',
    'dbsettings',
    'django_extensions',
    'django_filters', 
    'django_tables2',
    'debug_toolbar',
    'storages',
    'tinymce',
    # TODO: Add all auth for easy social media logins
]

INSTALLED_APPS = OPTIONAL_APPS + INSTALLED_APPS

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['config/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': ['django.templatetags.static'],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
DATABASES = {}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=False)


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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'config/static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'config/static/media')


# Custom Authentication
# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/

AUTH_USER_MODEL = 'base.User'

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'


# Django Debug Toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/index.html

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'localhost',)

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]


# TinyMCE
# https://django-tinymce.readthedocs.io/en/latest/

TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "menubar": False,
    "plugins": 'lists, link, anchor',
    "toolbar": 'undo redo | formatselect | '
    'bold italic underline link anchor backcolor | alignleft aligncenter '
    'alignright alignjustify | bullist numlist outdent indent | '
    'removeformat | help',
}


# AWS S3

# AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
# AWS_DOMAIN_NAME = f'http://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_LOCATION = 'static'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_URL = AWS_DOMAIN_NAME + '/static/'
# MEDIA_ROOT = os.path.join(BASE_DIR, "config/media/")
# MEDIA_URL = '/media/'


# Heroku
# https://devcenter.heroku.com/articles/django-app-configuration

# django_heroku.settings(locals())
# del DATABASES['default']['OPTIONS']['sslmode']
