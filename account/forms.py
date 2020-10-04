from django import forms
from django.contrib.auth.models import User#1
from .models import UserProfile

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):#2
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    class Meta:#3
        model=User#4
        fields=("username","email")

    def clean_password2(self):#5
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=("phone","birth")
