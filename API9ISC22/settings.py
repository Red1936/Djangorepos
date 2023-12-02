"""
Django settings for API9ISC22 project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^v=0$lbze5%shluqsmozco3)4%x2qh+6ggm8gfp!zbh9z9u6c1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'api',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
]
# Configuración de autenticación social para Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '7262792113733925'
SOCIAL_AUTH_FACEBOOK_SECRET = 'e0e06bb5564f0400e751ea03027e208b'

# Proveedores de cuentas sociales configurados, en este caso, para Facebook
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client_id': '7262792113733925',
            'secret': 'e0e06bb5564f0400e751ea03027e208b',
        }
    }
}

# Configuración de la biblioteca Crispy Forms para usar el paquete de plantillas Bootstrap 5
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]


ROOT_URLCONF = 'API9ISC22.urls'

TEMPLATES = [
    {
        # os.path.join(BASE_DIR, 'templates')
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'API9ISC22.wsgi.application'
# gunicorn controlisc.wsgi:application

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME':'dbred',
        'USER': 'red',
        'PASSWORD': '0SAc4lv6QGtoaG7IMnGEe4DLXokzWVgB',
        'HOST': 'oregon-postgres.render.com',  # O la dirección IP de tu servidor PostgreSQL
        'PORT': '5432',           # Deja en blanco para usar el puerto predeterminado (5432)
        
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME':'postgres',
        # 'USER': 'postgres',
        # 'PASSWORD': '',
        # 'HOST': 'localhost',  # O la dirección IP de tu servidor PostgreSQL
        # 'PORT': '5432',           # Deja en blanco para usar el puerto predeterminado (5432)
        
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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Redirección después del inicio de sesión exitoso
LOGIN_REDIRECT_URL = reverse_lazy('home')

# Configuración del modelo de usuario personalizado (descomentar y ajustar según sea necesario)
# AUTH_USER_MODEL = 'myapp.CustomUser'

# Configuración del backend de correo electrónico para el envío de correos electrónicos
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'victormanuel135613@gmail.com'
EMAIL_HOST_PASSWORD = 'dbuh omtv odfb isuq'  # Clave de la cuenta de correo electrónico

# Configuración de los backends de autenticación
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# settings.py

# Redirigir todas las solicitudes HTTP a HTTPS
SECURE_SSL_REDIRECT = True

# Utilizar cookies seguras para sesiones y CSRF
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
