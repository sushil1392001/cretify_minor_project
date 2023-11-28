from django import forms
from django.forms import ModelForm
from .products import Products


class Add_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name',  'category', 'description', 'image']
        # fields = '__all__'
