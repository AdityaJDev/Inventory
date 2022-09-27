from django.urls import path, include

from management.views import *

app_name = "management"

urlpatterns = [
    path("acc/<int:pk>", AccessoryShow.as_view(), name="shoaccessories"),
    path("", AssetShow.as_view(), name="show_info"),
    path("insert_asset/", AssetInsertView.as_view(), name="asset"),
    path("insert_accessory<int:pk>", AccessoryInsertView.as_view(), name="accessory"),
    path("update_asset/<int:pk>", AssetUpdateView.as_view(), name="upasset"),
    path(
        "update_accessory/<int:pk>", AccessoryUpdateView.as_view(), name="upaccessory"
    ),
    path("delete_asset/<int:pk>", AssetDeleteView.as_view(), name="delasset"),
    path(
        "delete_accessory/<int:pk>", AccessoryDeleteView.as_view(), name="delaccessory"
    ),
]
