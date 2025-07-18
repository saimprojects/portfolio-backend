from decouple import config
import dj_database_url
from pathlib import Path
import os
import cloudinary





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# cors

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='').split(',')
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='').split(',')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders', 
    'cloudinary',
    'cloudinary_storage',
    'ckeditor',

    #apps
    'core',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 🔼 move to top
    'django.middleware.common.CommonMiddleware',  # after cors
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL = '/media/'


#jazmin
JAZZMIN_SETTINGS = {
    "site_title": "Saim Portfolio Admin",
    "site_header": "Saim Potfolio",
    "site_brand": "Saim Portfolio",
    "welcome_sign": "Welcome to Saim Portfolio panel",
    "copyright": "meetsaim.online",
    "search_model": ["auth.User", "app.Product"],

    # Top Menu Links
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "app"},  # apki app ka naam
    ],

    # User Menu Links
    "usermenu_links": [
        {"name": "Support", "url": "https://t.me/yourtelegram", "new_window": True},
    ],

    # Side menu settings
    "show_sidebar": True,
    "navigation_expanded": True,

    # Custom icons (optional)
    "icons": {
        "auth": "fas fa-users",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users-cog",
    },

    # Change Theme Colors (Optional)
    "theme": "cosmo",  # Bootswatch theme use kar sakte ho (flatly, cyborg, cosmo etc.)

}


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

cloudinary.config(
  cloud_name=config("CLOUD_NAME"),
  api_key=config("API_KEY"),
  api_secret=config("API_SECRET")
)

