from tkinter import CASCADE
from django.db import models
from qux.core.models import CoreModel


class User(CoreModel):
    name = models.CharField(max_length=20)
    eid = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    asset_type = models.TextChoices(
        "Assets", "CPU Keyboard Monitor Mouse Printer Projector"
    )
    types = models.CharField(choices=asset_type.choices, blank=False, max_length=30)
    model_no = models.CharField(max_length=25)
    brand = models.CharField(max_length=30)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.DO_NOTHING)
    price = models.FloatField()

    def __str__(self):
        return self.brand


class Accessory(models.Model):
    accessory_type = models.CharField(max_length=50)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    model_no = models.CharField(max_length=25)

    def __str__(self):
        return self.accessory_type
