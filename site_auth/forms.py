from django import forms

class MyForm(forms.Form):
    my_name=forms.CharField(label='My name')