from django import forms
from product.models import Product, Tag

class ProductForm(forms.ModelForm):

    class Meta():
        model = Product
        fields = ('id','name', 'detail', 'category', 'price')

class TagForm(forms.ModelForm):

    class Meta:
        model  = Tag
        fields  = ('tag',) 

    