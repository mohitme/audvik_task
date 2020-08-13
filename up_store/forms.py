from django import forms

class upForm(forms.Form):
    name = forms.CharField(label='Table Name', max_length=20, required=True, help_text='Enter Table Name')
    file = forms.FileField(label='File', required=True, help_text='Upload File')