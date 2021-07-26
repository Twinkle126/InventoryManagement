from django.contrib import admin
from .models import Invoice

# Register your models here.


class InvoiceAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = [
        'seller',
        'buyer',
    ]


admin.site.register(Invoice, InvoiceAdmin)
