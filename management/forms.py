from management.models import *
from django.forms import ModelForm
from django.contrib.auth.models import User


class AddAccessoryForm(ModelForm):
    class Meta:
        model = Accessory
        fields = "__all__"
