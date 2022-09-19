from django.shortcuts import render
from django.views import View, generic
from .models import Accessory, Asset
from management.forms import AddAccessoryForm, AddAssetForm, AddUserForm


class AccessoryInsertView(View):
    def get(self, request):
        form = AddAccessoryForm()
        return render(request, "management/show_form.html", {"form": form})

    def post(self, request):
        message = ""
        form = AddAccessoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = AddAccessoryForm()
            message = "Accessory added"
        else:
            form = AddAccessoryForm()
            message = "Enter valid data"
        return render(
            request,
            "management/show_form.html",
            {"form": form, "message": message},
        )


class AssetInsertView(View):
    def get(self, request):
        form = AddAssetForm()
        return render(request, "management/show_form.html", {"form": form})

    def post(self, request):
        message = ""
        form = AddAssetForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = AddAssetForm()
            message = "Asset added"
        else:
            form = AddAssetForm()
            message = "Enter valid data"
        return render(
            request, "management/show_form.html", {"form": form, "message": message}
        )


class UserInsertView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, "management/show_form.html", {"form": form})

    def post(self, request):
        message = ""
        form = AddUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = AddUserForm()
            message = "User added"
        else:
            form = AddUserForm()
            message = "Enter valid data"
        return render(
            request, "management/show_form.html", {"form": form, "message": message}
        )


class DisplayView(View):
    def get(self, request):
        assets = Asset.objects.all().values("id", "types").distinct()

        return render(
            request,
            "management/display.html",
            {"assettypes": assets},
        )


class AssetShow(View):
    def get(self, request):
        _type = self.request.GET.get("type")
        info = Asset.objects.filter(types=_type).values()
        accessories = [Accessory.objects.filter(asset_id=x["id"]) for x in info]
        return render(
            request, "management/show_info.html", {"asset": info, "parts": accessories}
        )
