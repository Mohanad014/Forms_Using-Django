from django import forms
from .models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['name', 'email', 'password', 'contact_details']
