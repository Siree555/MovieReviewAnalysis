from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Searchform(forms.Form):
    search=forms.CharField(label="Search", max_length=100)

class CreateUserForm(UserCreationForm):
     class Meta:
         model = User
         fields= ['first_name','last_name','username','email','password1','password2']
