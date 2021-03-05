from django import forms
from .models import *



class UploadForm(forms.ModelForm):
    image=forms.ImageField(widget=forms.FileInput(attrs={"id" : "image"}))
    class Meta:
        model = Upload
        fields = ['image','title','tags',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Add title....", 'required': True, }),
            'image': forms.TextInput(attrs={'class': '','required': True, 'multiple': 'True' }),
            'tags': forms.TextInput(attrs={'class': '','required': True }),
        }
