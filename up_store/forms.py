from django import forms
from up_store.models import csv_file

class uploadForm(forms.ModelForm):
    class Meta:
        model = csv_file
        fields = ('description', 'file', )