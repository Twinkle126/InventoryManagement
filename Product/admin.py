from django.contrib import admin

from .models import Item

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = [
        'product_name',
        'quantity',
        'base_price',
        'tax',
        'amount',
    ]

admin.site.register(Item, ProductAdmin)
