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
                'placeholder': 'Choose a username',
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            return username.strip()
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            return email.strip().lower()
        return email


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={
            'class': 'neu-input',
            'placeholder': 'Enter username or email address',
            'autocomplete': 'username',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({
            'class': 'neu-input',
            'placeholder': 'Enter your password',
            'autocomplete': 'current-password',
        })

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            return username.strip()
        return username