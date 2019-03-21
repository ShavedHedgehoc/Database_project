import magic

from django import forms
from django.core.exceptions import ValidationError

class File_upload_form(forms.Form):
    filename = forms.FileField()
    def clean_filename(self):
        supported_types=[        
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "application/octet-stream",
        ]
        supported_extensions=[
            "xls",
            "xlsx",
            "xlsm",            
        ]
        supported_size=2*1024*1024    
        data=self.cleaned_data['filename']
        content_type = magic.from_buffer(data.read(), mime=True) 
        if content_type not in supported_types:
            raise forms.ValidationError('Формат файла не поддерживается. Файл не является файлом Excel')            
        file_size=data.size
        if file_size>supported_size:
            raise forms.ValidationError('Размер файла слишком большой (Размер > '+str(supported_size/(1024*1024))+' Mb)')
        file_extension=data.name.split('.')[-1]
        if file_extension not in supported_extensions:
            raise forms.ValidationError('Расширение не поддерживается. Допустимые расширения: ".xls", ".xlsx", ".xlsm"')
        return data


