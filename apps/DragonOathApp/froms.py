from django import forms
from django.forms import ModelForm
from apps.DragonOathApp import models

class LoginForm(ModelForm):
    class Meta:
        model = models.Userinfo
        fields = ['gmail', 'passwd']
        labels = {
            'gmail': '邮箱',
            'passwd': '密码'
        }
        widgets = {
            'gmail': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入邮箱'
            }),
            'passwd': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入密码'
            })
        }

class RegisterForm(ModelForm):
    class Meta:
        model = models.Userinfo
        fields = '__all__'
        labels = {
            'user_name': '用户名',
            'gmail': '邮箱',
            'passwd': '密码'
        }
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入用户名'
            }),
            'gmail': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入邮箱'
            }),
            'passwd': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入密码'
            })
        }

