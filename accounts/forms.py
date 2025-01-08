# forms.py
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'role', 'password']

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'role']



class CustomUserRegistrationForm(UserCreationForm):
    # Custom fields
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    role = "student"
    

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control'})


class CustomUserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']   # Only two fields are required for login


    
class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'role']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }