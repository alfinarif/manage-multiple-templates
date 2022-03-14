from .base import *


SECRET_KEY = config('SECRET_KEY')

DEBUG = False
ALLOWED_HOSTS = []



DATABASES = {
    'default': {},
    'accounts': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'accounts',
        'USER': 'postgres',
        'PASSWORD': 'alfin5555',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'blog': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blogs',
        'USER': 'postgres',
        'PASSWORD': 'alfin5555',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'store': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'single_vendor',
        'USER': 'postgres',
        'PASSWORD': 'alfin5555',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'vendor_store': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'multi_vendor',
        'USER': 'postgres',
        'PASSWORD': 'alfin5555',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'order': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'orders',
        'USER': 'postgres',
        'PASSWORD': 'alfin5555',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'dashboard': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dashboard',
        'USER': 'postgres',
        'PASSWORD': 'alfin5555',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'notification': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'notification',
        'USER': 'postgres',
        'PASSWORD': 'alfin5555',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DATABASE_ROUTERS = ['accounts.router.AccountsRouter', 'blog.router.BlogRouter', 'dashboard.router.DashboardRouter', 'store.router.SingleVendorRouter']
