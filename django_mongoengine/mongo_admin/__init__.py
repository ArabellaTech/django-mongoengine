from django.utils.module_loading import autodiscover_modules

from .options import DocumentAdmin, JSONDocumentAdmin
from .sites import site
from .decorators import register

__all__ = ['DocumentAdmin', 'JSONDocumentAdmin', 'site', 'register']


def autodiscover():
    autodiscover_modules('admin', register_to=site)


default_app_config = "django_mongoengine.mongo_admin.apps.MongoAdminConfig"
