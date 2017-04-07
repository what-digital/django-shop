# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.renderers import TemplateHTMLRenderer

from shop.models.cart import CartModel
from shop.serializers.cart import CartSerializer


class CatalogRenderer(TemplateHTMLRenderer):
    template_name = 'vanilla/catalog.html'

    def render(self, data, accepted_media_type=None, context=None):
        request = context['request']
        response = context['response']
        template_context = {}

        if response.exception:
            template = self.get_exception_template(response)
        else:
            view = context['view']
            template_names = self.get_template_names(response, view)
            template = self.resolve_template(template_names)
            template_context['paginator'] = view.paginator

        template_context['data'] = data
        self.update_with_cart_context(context)
        template_context.update(context)
        return template.render(template_context, request=request)

    def update_with_cart_context(self, context):
        try:
            cart = CartModel.objects.get_from_request(context['request'])
            context['is_cart_filled'] = cart.items.exists()
            cart_serializer = CartSerializer(cart, context=context, label='cart')
            context['cart'] = cart_serializer.data
        except (KeyError, CartModel.DoesNotExist):
            pass
