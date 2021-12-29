from django.db.models import fields
from .models import shop
from django import forms

class modeForm(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','disc','price','img']
