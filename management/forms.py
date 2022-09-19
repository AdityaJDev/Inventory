from management.models import *
from django.forms import ModelForm


class AddAssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = "__all__"


class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class AddAccessoryForm(ModelForm):
    class Meta:
        model = Accessory
        fields = "__all__"
