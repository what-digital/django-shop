# -*- coding: utf-8 -*-
"""
Loop over shipping backends defined in settings.SHOP_SHIPPING_BACKENDS and add
their URLs to the shipping namespace. eg:
http://www.example.com/shop/ship/dhl
http://www.example.com/shop/ship/fedex
...
"""
from django.conf.urls import include, url
from shop.backends_pool import backends_pool

urlpatterns = []

for backend in backends_pool.get_shipping_backends_list():
    regexp = "^%s/" % backend.url_namespace
    urls = backend.get_urls()
    # pattern = [url(regexp, include(backend.get_urls()))]

    urlpatterns.append(url(regexp, include(backend.get_urls())))

    print(urlpatterns)
