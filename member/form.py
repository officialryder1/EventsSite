from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUser(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        )

        # widgets = {
        #     'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
        #     'firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
        #     'lastname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
        #     'email': forms.EmailField()
        # }