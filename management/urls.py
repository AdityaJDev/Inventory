from django.urls import path, include

from management.views import *

app_name = "management"

urlpatterns = [
    path("", DisplayView.as_view(), name="display"),
    path("acc", AccessoryShow.as_view(), name="shoaccessories"),
    path("types", InsertAssetType.as_view(), name="typesofasset"),
    path("users/", DisplayUserView.as_view(), name="userlist"),
    path("info/", AssetShow.as_view(), name="show_info"),
    path("insert_user/", UserInsertView.as_view(), name="user"),
    path("insert_asset/", AssetInsertView.as_view(), name="asset"),
    path("insert_accessory", AccessoryInsertView.as_view(), name="accessory"),
    path("update_asset/<int:pk>", AssetUpdateView.as_view(), name="upasset"),
    path(
        "update_accessory/<int:pk>", AccessoryUpdateView.as_view(), name="upaccessory"
    ),
    path("update_user/<int:pk>", UserUpdateView.as_view(), name="upuser"),
    path("delete_asset/<int:pk>", AssetDeleteView.as_view(), name="delasset"),
    path(
        "delete_accessory/<int:pk>", AccessoryDeleteView.as_view(), name="delaccessory"
    ),
    path("delete_user/<int:pk>", UserDeleteView.as_view(), name="deluser"),
]
