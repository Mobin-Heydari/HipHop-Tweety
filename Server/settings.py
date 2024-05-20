from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tmg*2c3rl3j-arawl4+mctn*_q53uw8%y^y4b(0oy01soxynn('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.hip-hop-tweety.com', 'hip-hop-tweety.com']


# Application definition

INSTALLED_APPS = [
    # Admin panel third party app
    'jazzmin',
    
    # Contribs apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custome apps
    'home.apps.HomeConfig',
    'users.apps.UsersConfig',
    'alboms.apps.AlbomsConfig',
    'genres.apps.GenresConfig',
    'search.apps.SearchConfig',
    'payment.apps.PaymentConfig',
    'musices.apps.MusicesConfig',
    'landing.apps.LandingConfig',
    'profiles.apps.ProfilesConfig',
    'favorites.apps.FavoritesConfig',
    'subscription.apps.SubscriptionConfig',
    'authentication.apps.AuthenticationConfig',
    
    # PWA
    'pwa'
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

ROOT_URLCONF = 'Server.urls'

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
            'libraries': {
                'faver_validator': 'musices.templatetags.faver_validator',
                'faver_albume_validator': 'alboms.templatetags.faver_albume_validator',
            },
        },
    },
]

WSGI_APPLICATION = 'Server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hiphoptw_DataBase',                      
        'USER': 'hiphoptw_Hip_Hop_Tweety',
        'PASSWORD': 'k6=_JR(eD5ZB',
        'HOST' : '127.0.0.1',
        'PORT' : '3306'
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

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = '/home/hiphoptw/public_html/media'
STATIC_ROOT = '/home/hiphoptw/public_html/static'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Auth user model
AUTH_USER_MODEL = 'users.User'


# Emailing Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'venus.pws-dns.net'
EMAIL_HOST_USER = 'email@hip-hop-tweety.com'
EMAIL_HOST_PASSWORD = 't4xxohmp5o6t'
EMAIL_PORT = 587


#   Zarinpal --api--merchand
# SANDBOX MODE
MERCHANT = "00000000-0000-0000-0000-000000000000"
SANDBOX = True


# Service worker path
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')


# PWA manifest settings
PWA_APP_NAME = "Hip Hop Tweety"
PWA_APP_DESCRIPTION = "Hip Hop Tweety bigest music platform in iran"
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/images/pwa/logos/win/192x192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/images/pwa/logos/win/256x256.png',
        'sizes': '256x256'
    },
    {
        'src': '/static/images/pwa/logos/win/384x384.png',
        'sizes': '384x384'
    },
    {
        'src': '/static/images/pwa/logos/win/512x512.png',
        'sizes': '512x512'
    },
    
    # Androids
    {
        'src': '/static/images/pwa/logos/android/72x72.png',
        'sizes': '72x72'
    },
    {
        'src': '/static/images/pwa/logos/android/96x96.png',
        'sizes': '96x96'
    },
    
    {
        'src': '/static/images/pwa/logos/android/128x128.png',
        'sizes': '128x128'
    },
    
    {
        'src': '/static/images/pwa/logos/android/144x144.png',
        'sizes': '144x144'
    },
    
    {
        'src': '/static/images/pwa/logos/android/152x152.png',
        'sizes': '152x152'
    },
    
    {
        'src': '/static/images/pwa/logos/android/192x192.png',
        'sizes': '192x192'
    },
    
    {
        'src': '/static/images/pwa/logos/android/384x384.png',
        'sizes': '384x384'
    },
    
    {
        'src': '/static/images/pwa/logos/android/512x512.png',
        'sizes': '512x512'
    },
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/pwa/logos/ios/120x120.png',
        'sizes': '120x120'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icon.svg',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'rtl'
PWA_APP_LANG = 'fa-IR'