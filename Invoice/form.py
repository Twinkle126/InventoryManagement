# from Merchant.models import Seller
from django import forms
from .models import Invoice

# create a ModelForm
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"
