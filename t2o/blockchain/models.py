from django.db import models
import pandas as pd
from django.shortcuts import get_object_or_404


class CryptoCurrencies(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class FiatCurrencies(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class L3Version(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class L3(models.Model):
    TYPE_OF_ORDER = (
            ('BID', 'bids'),
            ('ASK', 'asks'),
    )

    version = models.ForeignKey(L3Version, on_delete=models.CASCADE)
    cryptocurrencies = models.ForeignKey(CryptoCurrencies, on_delete=models.CASCADE)
    fiatcurrencies = models.ForeignKey(FiatCurrencies, on_delete=models.CASCADE)
    order_type = models.CharField(choices=TYPE_OF_ORDER, max_length=3)
    price = models.FloatField(null=False)
    quantity = models.FloatField(null=False)
    number = models.IntegerField(null=False)

