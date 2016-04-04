# -*- coding: utf-8 -*-


def function_factory(field_name):
    def f(self, obj):
        return getattr(obj, field_name, None)
    f.short_description = field_name
    return f


def dynamic_fields_list_display(*field_names):
    """ adds dynamic fields to list display - useful for DynamicDocuments """
    def wrapper(cls):
        for field_name in field_names:
            name = '_get_%s' % field_name
            setattr(cls, name, function_factory(field_name))
            if isinstance(cls.list_display, list):
                cls.list_display = cls.list_display + [name]
            else:
                cls.list_display = cls.list_display + (name, )
        return cls
    return wrapper
