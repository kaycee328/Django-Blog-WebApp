from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ChangePassword(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    # firstname = forms.CharField(max_length=100)
    # lastname = forms.CharField(max_length=100)
    class Meta:
        model = Profile
        fields = ['image']
        # fields = ['image', 'firstname', 'lastname']