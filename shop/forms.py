from django import forms
from .models import Product

# Product form for Editing and Deletion
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'price',
            'stock',
            'available']

# Product form for new product creation
class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'name_alt',
            'category',
            'description',
            'price',
            'image',
            'stock',
            'available']