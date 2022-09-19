from django.urls import path, include

from management.views import *

app_name = "management"

urlpatterns = [
    path("", DisplayView.as_view(), name="display"),
    path("info/", AssetShow.as_view(), name="show_info"),
    path("insert_user/", UserInsertView.as_view(), name="user"),
    path("insert_asset/", AssetInsertView.as_view(), name="asset"),
    path("insert_accessory", AccessoryInsertView.as_view(), name="accessory"),
]
