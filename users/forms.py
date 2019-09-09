from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# creates a form that inherits from the UserCreationForm
class UserRegisterForm(UserCreationForm):
    # adds an email field to the form
    email = forms.EmailField()

    # creates nested namespace for configurations
    # says the model that will be affected is the User model
    # adds fields to the form in the specified order
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']