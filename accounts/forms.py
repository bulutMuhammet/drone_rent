from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# kullanıcı kayıt formu
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="Ad")
    last_name = forms.CharField(label="Soyad")
    email = forms.EmailField(label="E-posta")


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

