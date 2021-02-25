from django import forms
from .models import Product, CatProd

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'name_alt',
            'description',
            'price',
            'image',
            'stock',]

class CatProdForm(forms.ModelForm):
    class Meta:
        model = CatProd
        fields = [
            'category',
            'product']