from django.urls import path, include
from .views import (
    GeneratePDF,
    BuyerViewSet,
    SellerViewSet,
    render_pdf_view,
    buyer_view,
    seller_view,
)
from rest_framework.routers import DefaultRouter


app_name = 'merchant'

router = DefaultRouter()
router.register(
    '',
    BuyerViewSet,
    basename='Buyer',
)

router1 = DefaultRouter()
router1.register(
    '',
    SellerViewSet,
    basename='Seller',
)


urlpatterns = [
    path('', buyer_view, name='buyer_view'),
    path('seller_view/', seller_view, name='seller_view'),
    path('mypdf/', GeneratePDF.as_view(), name='mypdf'),
    path('my-view/', render_pdf_view, name='my-view'),
    path('buyer/', include(router.urls)),
    path('seller/', include(router1.urls)),
]
