# -*- coding: utf-8 -*-
"""
Loop over payment backends defined in settings.SHOP_PAYMENT_BACKENDS and add
their URLs to the payment namespace. eg:
http://www.example.com/shop/pay/paypal
http://www.example.com/shop/pay/pay-on-delivery
...
"""
from django.conf.urls import include, url
from shop.backends_pool import backends_pool

urlpatterns = []

# For every backend defined in the backend pool, load all the URLs it defines
# in its get_urls() method.
for backend in backends_pool.get_payment_backends_list():
    regexp = '^%s/' % backend.url_namespace

    urlpatterns.append(url(regexp, include(backend.get_urls())))
