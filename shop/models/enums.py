# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import enum
from six import with_metaclass, string_types
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy


class ChoiceEnumMeta(enum.EnumMeta):
    def __call__(cls, value, *args, **kwargs):
        if isinstance(value, string_types):
            try:
                value = cls.__members__[value]
            except KeyError:
                pass  # let the super method complain
        return super(ChoiceEnumMeta, cls).__call__(value, *args, **kwargs)


@python_2_unicode_compatible
class ChoiceEnum(with_metaclass(ChoiceEnumMeta, enum.Enum)):
    """
    Utility class to handle choices in Django model fields
    """
    def __str__(self):
        return self.name

    @classmethod
    def choices(cls):
        values = [p.value for p in cls.__members__.values()]
        if len(values) > len(set(values)):
            msg = "Duplicate values found in {}".format(cls.__class__.__name__)
            raise ValueError(msg)
        choices = [(prop.value, ugettext_lazy('.'.join((cls.__name__, attr))))
                   for attr, prop in cls.__members__.items()]
        return choices
