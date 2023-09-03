from django import forms
from .models import Product


class NewProduct(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['seller', 'slug']
        widgets = {
        }
