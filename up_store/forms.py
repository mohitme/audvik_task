from django import forms
from django.core.validators import FileExtensionValidator

class upForm(forms.Form):
    name = forms.CharField(label='Table Name', max_length=20, required=True, help_text='Enter Table Name')
    file = forms.FileField(label='File', required=True, validators=[FileExtensionValidator(allowed_extensions=['csv'])])