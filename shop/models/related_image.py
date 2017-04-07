# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from six import with_metaclass

from django.db import models
from django.utils.translation import ugettext_lazy

from filer.fields import image

from shop.models.product import BaseProduct
from shop import deferred


class BaseProductImage(with_metaclass(deferred.ForeignKeyBuilder, models.Model)):
    """
    ManyToMany relation from the polymorphic Product to a set of images.
    """
    image = image.FilerImageField()
    product = deferred.ForeignKey(BaseProduct)
    order = models.SmallIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True
        verbose_name = ugettext_lazy("Product Image")
        verbose_name_plural = ugettext_lazy("Product Images")
        ordering = ('order',)

ProductImageModel = deferred.MaterializedModel(BaseProductImage)
