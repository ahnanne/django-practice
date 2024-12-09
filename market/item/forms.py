from django import forms

from .models import Item

INPUT_STYLE = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_STYLE
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_STYLE
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_STYLE
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_STYLE
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_STYLE
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_STYLE
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_STYLE
            }),
        }
