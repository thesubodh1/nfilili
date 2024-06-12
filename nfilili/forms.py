from django import forms
from .models import EmailRegister,DetailRegistration

class EmailRegistrationForm(forms.ModelForm):
    class Meta:
        model = EmailRegister
        fields = "__all__"
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }

class DetailRegistrationForm(forms.ModelForm):
    class Meta:
        model = DetailRegistration
        exclude = ["email","latitude","longitude"]
        widgets = {
            "full_name" : forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            "business_name" : forms.TextInput(attrs={'placeholder': 'Enter your business name'}),
            "description" : forms.Textarea(attrs={'placeholder': 'Define your business'}),
            "location" : forms.TextInput(attrs={'placeholder': 'paste your google map location'})
        }
