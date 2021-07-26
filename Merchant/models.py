from django.db import models

# Create your models here.


class Buyer(models.Model):
    buyer_name = models.CharField(max_length=50)
    buyer_address = models.TextField(max_length=200, blank=True, null=True)
    buyer_phone = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.buyer_name


class Seller(models.Model):
    seller_name = models.CharField(max_length=50)
    seller_address = models.TextField(max_length=200, blank=True, null=True)
    seller_phone = models.IntegerField(blank=True, null=True)
    signature = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.seller_name
