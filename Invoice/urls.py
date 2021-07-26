from django.db import router
from django.urls import path, include
from .views import InvoiceViewSet
from rest_framework.routers import DefaultRouter

app_name = 'Invoice'

router = DefaultRouter()
router.register(
    '',
    InvoiceViewSet,
    basename='Invoices',
)

urlpatterns = [
    # path('product_view/', product_view, name='home_view'),
    path('invoice/', include(router.urls)),
]
