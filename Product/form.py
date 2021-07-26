from django import forms
from .models import Item

# create a ModelForm
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
