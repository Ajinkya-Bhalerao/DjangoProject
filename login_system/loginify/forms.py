from django import forms
from . models import UserDetails
class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('username', 'email', 'password')
        
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('email', 'password')