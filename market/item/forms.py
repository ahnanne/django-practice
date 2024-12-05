from django import forms

from .models import Item

INPUT_STYLE = 'w-full py-4 px-6 rounded-xl'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
