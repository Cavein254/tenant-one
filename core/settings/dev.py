from .base import *


DEGUB = TRUE

ALLOWED_HOSTS = [*]


INSTALLED_APPS = INSTALLED_APPS

MIDDLEWARE = ['db_multitenant.middleware.MultiTenantMiddleware',] + MIDDLEWARE

DATABASES = {
    'default': {
        'ENGINE': 'db_multitenant.middleware.MultiTenantMiddleware',
        'NAME': "tenants",
        'USER': "myuser",
        'PASSWORD': "mysuperpassword",
        'HOST': "localhost",
        "PORT": "3306",
    }
}
