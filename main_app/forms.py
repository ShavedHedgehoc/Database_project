from django import forms

from django import forms

class File_upload_form(forms.Form):
    filename = forms.FileField()