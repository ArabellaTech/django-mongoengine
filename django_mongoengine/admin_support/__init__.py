# -*- coding: utf-8 -*-
""" set of hacks that allows to plug mongoengine Documents & DynamicDocuments to standard django admin """
from django.conf import settings

if 'django_mongoengine.admin_support' in settings.INSTALLED_APPS:
    from django.contrib.admin.sites import AdminSite
    from django.contrib.admin.checks import ModelAdminChecks
    from django_mongoengine.document import DynamicDocument
    from mongoengine.base.metaclasses import TopLevelDocumentMetaclass, DocumentMetaclass

    def patched_register(self, model_or_iterable, admin_class=None, **options):
        """ patch for registering Document to admin """
        if isinstance(model_or_iterable, TopLevelDocumentMetaclass) or isinstance(model_or_iterable, DocumentMetaclass):
            model_or_iterable = [model_or_iterable]
        return self.orig_register(model_or_iterable, admin_class, **options)

    AdminSite.orig_register = AdminSite.register
    AdminSite.register = patched_register
