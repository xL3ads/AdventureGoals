from django import forms
from Objective.models import Objective

class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = '__all__'
        exclude = ('user','completed')

        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload an image'}),
    }
