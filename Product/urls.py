from django.db import router
from django.urls import path, include
from .views import (
    GeneratePDF,
    ItemViewSet,
    ProductListView,
    product_render_pdf_view,
    product_view,
)
from rest_framework.routers import DefaultRouter

app_name = 'product'

router = DefaultRouter()
router.register(
    '',
    ItemViewSet,
    basename='Items',
)


urlpatterns = [
    path('product_view/', product_view, name='home_view'),
    path('pdf/', GeneratePDF.as_view(), name='pdf'),
    path('product_list_pdf/', ProductListView.as_view(), name='product_list_pdf'),
    path('product_pdf_/<pk>', product_render_pdf_view, name='product_pdf'),
    path('item/', include(router.urls)),
]
