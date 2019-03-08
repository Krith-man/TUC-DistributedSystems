"""
Django settings for AuthService project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xircmw@0g55z79pz#c!as)@j=%ojxny405gb877^=fxqd1qa02'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['snf-815302.vm.okeanos.grnet.gr',
                 'snf-815307.vm.okeanos.grnet.gr',
                 'snf-815301.vm.okeanos.grnet.gr',
                 'snf-815317.vm.okeanos.grnet.gr',
                 '127.0.0.1', ]

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'App',
	'API',
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

ROOT_URLCONF = 'AuthService.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')]
		,
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

WSGI_APPLICATION = 'AuthService.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

# ZooKeeper Configuration
ZOOKEEPER_NODE_ID = 'TUCleryAuth1'
ZOOKEEPER_HOST = 'snf-815301.vm.okeanos.grnet.gr'
ZOOKEEPER_USER = 'username'
ZOOKEEPER_PASSWORD = 'password'
ZOOKEEPER_ROOT = '/TUClery/'
ZOOKEEPER_PATH_TO_NODE = 'Auth/'
ZOOKEEPER_NODE_EPHIMERAL = True
# SERVER_HOSTNAME = 'snf-815302.vm.okeanos.grnet.gr'
# SERVER_PORT = '8000'
# Todo: Fix SERVER_HOSTNAME and SERVER_PORT
SERVER_HOSTNAME = 'http://127.0.0.1'
SERVER_PORT = '8003'
SHARED_KEY_BASE_64 = 'UziKLGN2cWPns4SzwkPEeGxH/SQS5oOYqIrF2h7WbGs='
AUTH_SYSTEM = 'TUClery'


# ZOOKEEPER_NODE_ID = 'SKAUTH2'
# ZOOKEEPER_HOST = 'snf-815301.vm.okeanos.grnet.gr'
# ZOOKEEPER_USER = 'username'
# ZOOKEEPER_PASSWORD = 'password'
# ZOOKEEPER_ROOT = '/TUClery/'
# ZOOKEEPER_PATH_TO_NODE = 'Auth/'
# ZOOKEEPER_NODE_EPHIMERAL = False
# SERVER_HOSTNAME = 'http://snf-816668.vm.okeanos.grnet.gr/authservicepython'
# SERVER_PORT = ''
# SHARED_KEY_BASE_64 = 'UziKLGN2cWPns4SzwkPEeGxH/SQS5oOYqIrF2h7WbGs='
# AUTH_SYSTEM = 'SKSYSTEM2'
