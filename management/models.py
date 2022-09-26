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
        return reverse("management:show_info")


class Asset(CoreModel):
    types = models.ForeignKey(
        AssetTypes, on_delete=models.DO_NOTHING, verbose_name="Type"
    )
    model_no = models.CharField(max_length=25, verbose_name="Model Number")
    brand = models.CharField(max_length=30, verbose_name="Brand")
    user = models.ForeignKey(
        User,
        null=True,
        default=None,
        blank=True,
        on_delete=models.DO_NOTHING,
        verbose_name="Allotted to",
    )
    price = models.FloatField(verbose_name="Price")

    def __str__(self):
        return self.brand + str(self.id)

    def get_absolute_url(self):
        return reverse("management:show_info")


class Accessory(CoreModel):
    accessory_type = models.CharField(max_length=50, verbose_name="Type")
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, verbose_name="Accessory of"
    )
    model_no = models.CharField(max_length=25, verbose_name="Model Number")

    def get_absolute_url(self):
        return reverse("management:show_info")

    def __str__(self):
        return self.accessory_type
