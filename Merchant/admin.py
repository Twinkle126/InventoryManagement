from django.contrib import admin
from .models import Seller, Buyer

# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = [
        'seller_name',
        'seller_address',
        'seller_phone',
    ]


class BuyerAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = [
        'buyer_name',
        'buyer_address',
        'buyer_phone',
    ]


admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Seller, SellerAdmin)
