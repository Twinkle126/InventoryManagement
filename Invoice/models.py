from typing import FrozenSet
from django.db import models

from Merchant.models import Buyer, Seller

# Create your models here.


class Invoice(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True, blank=True)


# class OrderLine(models.Model):
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     item=models.ForeignKey(Item,)
