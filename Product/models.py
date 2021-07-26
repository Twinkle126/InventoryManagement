from Invoice.models import Invoice
from django.db import models

# from Merchant.models import Buyer, Seller


# Create your models here.
class Item(models.Model):
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField(blank=True, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    base_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True, blank=True)

    @property
    def amount(
        self,
    ):
        """
        returns the total amount.
        """
        if self.base_price:
            return self.base_price + self.tax
        else:
            return 0

    def __str__(self):
        return self.product_name
