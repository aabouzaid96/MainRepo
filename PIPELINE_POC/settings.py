import os
import sys

from pathlib import Path

from tutorial.settings import BASE_DIR


ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'PIPELINE_POC.urls'
DEBUG = True
SECRET_KEY = ')in4_vc0h2*29pq=4zvp!)f7+bjgs38&3e+cei$%=4zvphaez&'
AUTH_USER_MODEL = 'accounts.User'
# Static files (CSS, JavaScript, Images)
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'


# Add Repo-A and Repo-B to the Python path
sys.path.append(str(BASE_DIR / "RepoA"))
sys.path.append(str(BASE_DIR / "RepoB"))

INSTALLED_APPS = [
    # other apps
    'django.contrib.admin',  # Required for the admin interface
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # For REST APIs
    'add_users',
    'accounts',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',  # This must come before AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='pipeline_poc'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='postgresAWS0'),
        'HOST': config('DB_HOST', default='172.31.37.63'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add your custom templates directory here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by the admin app
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]