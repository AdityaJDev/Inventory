from tkinter import CASCADE
from django.db import models
from qux.core.models import CoreModel
from django.urls import reverse
from django.contrib.auth.models import User


class AssetTypes(CoreModel):
    type_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type_name

    def get_absolute_url(self):
        return reverse("management:display")


class Asset(CoreModel):
    types = models.ForeignKey(AssetTypes, on_delete=models.DO_NOTHING)
    model_no = models.CharField(max_length=25)
    brand = models.CharField(max_length=30)
    user = models.ForeignKey(
        User, null=True, default=None, blank=True, on_delete=models.DO_NOTHING
    )
    price = models.FloatField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse("management:display")


class Accessory(CoreModel):
    accessory_type = models.CharField(max_length=50)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    model_no = models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse("management:display")

    def __str__(self):
        return self.accessory_type
