from django import forms

class File_upload_form(forms.Form):
    filename = forms.FileField(label="123")
