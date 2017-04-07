# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from six import with_metaclass

from django.db import models
from django.utils.translation import ugettext_lazy

from cms.models.pagemodel import Page

from shop.models.product import BaseProduct
from shop import deferred


class BaseProductPage(with_metaclass(deferred.ForeignKeyBuilder, models.Model)):
    """
    ManyToMany relation from the polymorphic Product to the CMS Page.
    This in practice is the category.
    """
    page = models.ForeignKey(Page)
    product = deferred.ForeignKey(BaseProduct)

    class Meta:
        abstract = True
        unique_together = ('page', 'product',)
        verbose_name = ugettext_lazy("Category")
        verbose_name_plural = ugettext_lazy("Categories")

ProductPageModel = deferred.MaterializedModel(BaseProductPage)
