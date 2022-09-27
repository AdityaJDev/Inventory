from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views import View, generic
from .models import Accessory, Asset, AssetTypes
from .forms import AddAccessoryForm
from django.http import HttpResponseRedirect


class AccessoryInsertView(generic.CreateView):
    model = Accessory
    fields = ["accessory_type", "model_no"]
    template_name = "management/show_form.html"

    def post(self, request, **kwargs):
        pk = kwargs["pk"]
        d = request.POST.copy()
        d["asset"] = pk
        form = AddAccessoryForm(d or None)
        if form.is_valid():
            form.save()
        url = reverse("management:shoaccessories", kwargs={"pk": pk})
        return HttpResponseRedirect(url)


class AccessoryDeleteView(generic.DeleteView):
    model = Accessory
    fields = "__all__"
    template_name = "management/show_form.html"
    success_url = reverse_lazy("management:show_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Are you sure you want to delete ?"
        accessory = Accessory.objects.filter(id=self.object.id).values()
        accessorytype = Asset.objects.get(id=self.object.asset_id)
        context["list"] = accessory
        context["type"] = accessorytype
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().get(self, request, *args, **kwargs)
        else:
            return render(
                request, "management/show_form.html", {"message": "Access Denied"}
            )

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.success_url = reverse_lazy(
                "management:shoaccessories",
                kwargs={"pk": Accessory.objects.get(id=kwargs.get("pk")).asset_id},
            )
            return super().post(self, request, *args, **kwargs)
        else:
            return render(
                request, "management/show_form.html", {"message": "Access Denied"}
            )


class AssetDeleteView(generic.DeleteView):
    model = Asset
    fields = "__all__"
    template_name = "management/show_form.html"
    success_url = reverse_lazy("management:show_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Are you sure you want to delete ?"
        asset = Asset.objects.filter(id=self.object.id).values()
        assettype = AssetTypes.objects.get(id=self.object.types_id)
        context["type"] = assettype
        context["list"] = asset
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().get(self, request, *args, **kwargs)
        else:
            return render(
                request, "management/show_form.html", {"message": "Access Denied"}
            )

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().post(self, request, *args, **kwargs)
        else:
            return render(
                request, "management/show_form.html", {"message": "Access Denied"}
            )


class AssetInsertView(generic.CreateView):
    model = Asset
    fields = "__all__"
    template_name = "management/show_form.html"


class AssetUpdateView(generic.UpdateView):
    model = Asset
    fields = "__all__"
    template_name = "management/show_form.html"
    success_url = reverse_lazy("management:show_info")

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().get(self, request, *args, **kwargs)
        else:
            return render(
                request, "management/show_form.html", {"message": "Access Denied"}
            )

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().post(self, request, *args, **kwargs)
        else:
            return render(
                request, "management/show_form.html", {"message": "Access Denied"}
            )


class AccessoryUpdateView(generic.UpdateView):
    model = Accessory
    fields = "__all__"
    template_name = "management/show_form.html"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse_lazy(
            "management:shoaccessories", kwargs={"pk": request.POST.get("asset")}
        )
        return super().post(self, request, *args, **kwargs)


class AssetShow(View):
    def get(self, request):
        info = Asset.objects.all()
        headerlist = [
            y.verbose_name
            for y in info[0]._meta.fields
            if (y.name != "dtm_created") and (y.name != "dtm_updated")
        ]
        return render(
            request,
            "management/show_info.html",
            {
                "asset": info,
                "header": headerlist,
            },
        )


class DisplayView(View):
    def get(self, request):
        assets = AssetTypes.objects.filter(
            id__in=[x["types"] for x in Asset.objects.all().values("types").distinct()]
        )
        return render(
            request,
            "management/display.html",
            {"assettypes": assets},
        )


class AccessoryShow(View):
    def get(self, request, **kwargs):
        pk = kwargs["pk"]
        message = ""
        accessories = Accessory.objects.filter(asset_id=pk)
        asset = Asset.objects.filter(id=pk).values()
        assettype = AssetTypes.objects.get(id=asset[0]["types_id"])
        accheaderlist = []
        if accessories.exists():
            accheaderlist = [
                y.verbose_name
                for y in accessories[0]._meta.fields
                if (y.name != "dtm_created") and (y.name != "dtm_updated")
            ]
        else:
            message = "No accessories for this asset"
        return render(
            request,
            "management/parts.html",
            {
                "parts": accessories,
                "header": accheaderlist,
                "message": message,
                "pk": pk,
                "asset": asset,
                "type": assettype,
            },
        )
