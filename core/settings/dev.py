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

MULTITENANT_MAPPER_CLASS = 'core.mapper.TenantMapper'

"""
These commands are required by django-db-multitenants for management
commands to work
"""

from db_multitenants.utils import update_from_env
update_from_env(database_settings=DATABASES[default])
