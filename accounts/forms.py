from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).count() == 0:
            return email
        raise forms.ValidationError("Email ya registrado")
            


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')