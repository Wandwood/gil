from socket import fromshare
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Password',
        widget = forms.PasswordInput(
            attrs={
                "id": "user-password",
                'cols': 80, 'rows': 20
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget = forms.PasswordInput(
            attrs={
                "id": "user-confirm-password",
                'cols': 80, 'rows': 20
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another")
        return username 

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This is an invalid email, please pick another")
        return email 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={
            "id": "user-password"
            })
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user")
        return username 