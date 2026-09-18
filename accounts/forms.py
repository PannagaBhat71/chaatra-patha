from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'neu-input',
                'placeholder': 'Enter your username',
                'autocomplete': 'username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'neu-input',
                'placeholder': 'Enter your email address',
                'autocomplete': 'email',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['password1', 'password2']:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'class': 'neu-input',
                    'placeholder': 'Enter password' if field_name == 'password1' else 'Confirm password',
                })


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'neu-input',
            'placeholder': 'Enter your username',
            'autocomplete': 'username',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'neu-input',
            'placeholder': 'Enter your password',
            'autocomplete': 'current-password',
        })