from django import forms

from news.models import MyUserModel


class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUserModel
        fields = '__all__'

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUserModel
        fields = ['username', 'password']