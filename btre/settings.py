
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dy86ybpww^fkz)w@!63t#s7c6vy0lg_(_pz!g3=_19-fl33e3a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Creating The Pages App -  2:30 We are going to put "pages.apps.PagesConfig" into installed apps. He got this from "apps.py" in pages. @3:40ish he talks about how autopep3 might come up when you save this and you should just install it in the virtual environment. @4:10 close that up and now he wants to create a urls.py file for the pages app. <create file called "urls.py" in the pages folder and go to it)
# Application definition

# Application definition

INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'btre.urls'

#Pages Templates & Base Layout - 00:39 you want to go down to here, with all the key value pairs and it has the "DIRS". Which is where we want go. 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#Pages Templates & Base Layout - 00:47 we want to tell templates where to look. Brad says he puts his templates in the root and not in the pages or anything and to let it know that we are going to say "os.path.join(BASE_DIR, 'templates')" BASE_DIR means base directory and the folder name we want to use is "templates".
#@1:20 then we want to go into the root of the project and create a folder called "Templates" and go there. He also talks about how it's up to you how to organize templates but he likes to categorize them by application and has a folder within there for that. @1:40 create a folder within Templates called page, we then created an index and about html file inside that folder. (2:06 go to Templates.Pages folder and input the <h1> tags in the html files) (2:15 go to pages/urls.py)
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

WSGI_APPLICATION = 'btre.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

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
