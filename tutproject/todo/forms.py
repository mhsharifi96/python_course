
from django import forms
from .models import person

class SimpleForm(forms.Form):
    title = forms.CharField( max_length=10, )
    description = forms.CharField( max_length=10,widget=forms.Textarea)


