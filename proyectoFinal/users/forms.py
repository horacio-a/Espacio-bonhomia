from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        help_texts = {k:'' for k in fields} # Saca los comentarios de ayuda

class Formulario_profile(forms.Form):
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)


class Formulario_profileImage(forms.Form):
    image = forms.ImageField(required=False)
