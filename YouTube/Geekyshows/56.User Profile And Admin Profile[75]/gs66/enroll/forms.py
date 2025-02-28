from django.contrib.auth.forms import User,UserCreationForm,UserChangeForm
from django import forms

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'email':'Email'}

class EditAdminProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}