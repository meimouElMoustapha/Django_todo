from django import forms
from django.forms import widgets 

from .models import Product

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name','description','detail','image']
        
        # widgets = {
        #     'name': forms(attrs={'class': 'form-control'}),
        #     'description': forms(attrs={'class': 'form-control'}),
        #     'detail': forms(attrs={'class': 'form-control'}),
        #     'image': forms(attrs={'class': 'form-control'}),
            
        # }
    