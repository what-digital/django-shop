from django.conf.urls import url

from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer

from shop.rest.money import JSONRenderer
from shop.views.catalog import ProductListView, SyncCatalogView
from shop.views.order import OrderView

from vanilla.serializers import ProductSummarySerializer
from vanilla.views.catalog import CatalogRenderer

urlpatterns = [
    url(
        r'^catalog/$',
        ProductListView.as_view(
            renderer_classes=(CatalogRenderer, JSONRenderer, BrowsableAPIRenderer),
            serializer_class=ProductSummarySerializer,
        )
    ),
    url(
        r'^catalog/sync-catalog$',
        SyncCatalogView.as_view(
            serializer_class=SyncCatalogSerializer,
        ),
        name='cm-sync-catalog',
    ),
    url(
        r'^checkout/',
        CheckoutView.as_view(),
        name='cm-checkout',
    ),
    url(
        r'^order/$',
        OrderView.as_view(
            renderer_classes=(TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer),
        ),
        name='cm-order-list',
    ),
    url(
        r'^order/(?P<slug>[\w-]+)/?$',
        OrderView.as_view(many=False),
        name='cm-order-detail',
    ),
]
