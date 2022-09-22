from django.urls import reverse, reverse_lazy
from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View, generic
from .models import Accessory, Asset
from django.contrib.auth.models import User
from .forms import AddAssetForm
from django.http import HttpResponseRedirect


class AccessoryInsertView(generic.CreateView):
    model = Accessory
    fields = "__all__"
    template_name = "management/show_form.html"


class AccessoryDeleteView(generic.DeleteView):
    model = Accessory
    fields = "__all__"
    template_name = "management/show_form.html"
    success_url = reverse_lazy("management:display")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Are you sure you want to delete ?"
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


class AssetDeleteView(generic.DeleteView):
    model = Asset
    fields = "__all__"
    template_name = "management/show_form.html"
    success_url = reverse_lazy("management:display")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Are you sure you want to delete ?"
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


class UserDeleteView(generic.DeleteView):
    model = User
    fields = "__all__"
    template_name = "management/show_form.html"
    success_url = reverse_lazy("management:userlist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Are you sure you want to delete ?"
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

    # def post(self, request):
    #     form = AddAssetForm(request.POST or None)
    #     if form.is_valid():
    #         print(request.POST)
    #         form.save()
    #         form = AddAssetForm()
    #     url = reverse("management:show_info") + "?type=" + request.POST.get("types")
    #     print(url)
    #     return HttpResponseRedirect(url)


class UserInsertView(generic.CreateView):
    model = User
    fields = "__all__"
    template_name = "management/show_form.html"
    success_url = reverse_lazy("management:display")

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


class AssetUpdateView(generic.UpdateView):
    model = Asset
    fields = "__all__"
    template_name = "management/show_form.html"
    success_url = reverse_lazy("management:display")

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


class UserUpdateView(generic.UpdateView):
    model = User
    fields = "__all__"
    template_name = "management/show_form.html"
    success_url = reverse_lazy("management:userlist")

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


class AssetShow(View):
    def get(self, request):
        _type = self.request.GET.get("type")
        info = Asset.objects.filter(types=_type)
        headerlist = [
            y.name
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
        assets = Asset.objects.all().values("types").distinct()
        return render(
            request,
            "management/display.html",
            {"assettypes": assets},
        )


class DisplayUserView(generic.ListView):
    model = User
    template_name = "management/show_users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class AccessoryShow(View):
    def get(self, request):
        pk = self.request.GET.get("pk")
        message = ""
        accessories = Accessory.objects.filter(asset_id=pk)
        accheaderlist = []
        if accessories.exists():
            accheaderlist = [
                y.name
                for y in accessories[0]._meta.fields
                if (y.name != "dtm_created") and (y.name != "dtm_updated")
            ]
        else:
            message = "No accessories for this asset"
        return render(
            request,
            "management/parts.html",
            {"parts": accessories, "header": accheaderlist, "message": message},
        )
