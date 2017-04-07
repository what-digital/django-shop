# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

# import default models from shop to materialize them
from shop.models.defaults.address import ShippingAddress, BillingAddress
from shop.models.defaults.cart import Cart
from shop.models.defaults.cart_item import CartItem
from shop.models.defaults.customer import Customer

__all__ = ['ShippingAddress', 'BillingAddress', 'Cart', 'CartItem', 'Customer', 'OrderItem',
           'Commodity', 'SmartCard', 'SmartPhoneModel', 'SmartPhone', 'Delivery', 'DeliveryItem']

# models defined by the myshop instance itself
if settings.SHOP_TUTORIAL == 'commodity' or settings.SHOP_TUTORIAL == 'i18n_commodity':
    from shop.models.defaults.order_item import OrderItem
    from shop.models.defaults.commodity import Commodity

elif settings.SHOP_TUTORIAL == 'smartcard':
    from shop.models.defaults.order_item import OrderItem
    from myshop.models.smartcard import SmartCard

elif settings.SHOP_TUTORIAL == 'i18n_smartcard':
    from shop.models.defaults.order_item import OrderItem
    from myshop.models.i18n_smartcard import SmartCard

elif settings.SHOP_TUTORIAL == 'polymorphic':
    from myshop.models.polymorphic_.order import OrderItem
    from myshop.models.polymorphic_.product import Product
    from myshop.models.polymorphic_.smartcard import SmartCard
    from myshop.models.polymorphic_.smartphone import SmartPhoneModel, SmartPhone

elif settings.SHOP_TUTORIAL == 'i18n_polymorphic':
    from myshop.models.i18n_polymorphic.order import OrderItem
    from myshop.models.i18n_polymorphic.product import Product
    from myshop.models.i18n_polymorphic.smartcard import SmartCard
    from myshop.models.i18n_polymorphic.smartphone import SmartPhoneModel, SmartPhone

if settings.SHOP_TUTORIAL in ['polymorphic', 'i18n_polymorphic']:
    from shop.models.defaults.delivery import Delivery, DeliveryItem
    __all__.extend(['Product', 'SmartCard', 'SmartPhoneModel', 'SmartPhone', 'Delivery', 'DeliveryItem'])
