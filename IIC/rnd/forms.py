from django.forms import ModelForm
from django import forms
from .models import basicDetails
from django.contrib.auth.models import User

class basicDetailsForm(ModelForm):
    class Meta:
        model = basicDetails
        fields = "__all__"
        widgets = {
            'googleScholar': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post description...',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
            'orcid': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post description...',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
            'scopusid': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post description...',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
            'researchid': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post description...',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
            'vidwanPortal': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post description...',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            

        }
        exclude = ["faculty"]        
