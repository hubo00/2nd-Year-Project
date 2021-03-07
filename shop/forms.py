from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'name_alt',
            'category',
            'description',
            'price',
            'image',
            'stock',]
