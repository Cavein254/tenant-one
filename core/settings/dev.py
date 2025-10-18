from .base import *  # noqa
import pymysql

pymysql.install_as_MySQLdb()


DEGUB = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = INSTALLED_APPS + [
    "user",
]  # noqa

MULTITENANT_MAPPER_CLASS = "core.mapper.TenantMapper"


MIDDLEWARE = [
    "db_multitenant.middleware.MultiTenantMiddleware",
] + MIDDLEWARE  # noqa

DATABASES = {
    "default": {
        "ENGINE": "db_multitenant.db.backends.mysql",
        "NAME": "tenants",
        "USER": "myuser",
        "PASSWORD": "mysuperpassword",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

DB_MULTITENANT_DEFAULT_DB = "tenants"

"""
These commands are required by django-db-multitenants for management
commands to work
"""

from db_multitenant.utils import update_from_env

update_from_env(database_settings=DATABASES["default"])
