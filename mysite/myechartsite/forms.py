#coding=utf-8
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    # gender = (
    #         ('male', "男"),
    #         ('female', "女"),
    # )
    levelchoices = (
        ('customer', "个人用户"),
        ('doctor', "专科医生"),
        ('expert', "疾控专家"),
    )

    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    level = forms.ChoiceField(label="用户类别", choices=levelchoices)
    location = forms.CharField(label="所在地", max_length=128)
    password1 = forms.CharField(label="密码", max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'} ))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # sex = forms.ChoiceField(label='性别', choices=gender)

class ChangeForm(forms.Form):
    # gender = (
    #         ('male', "男"),
    #         ('female', "女"),
    # )
    # levelchoices = (
    #     ('customer', "个人用户"),
    #     ('doctor', "专科医生"),
    #     ('expert', "疾控专家"),
    # )

    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # level = forms.ChoiceField(label="用户类别", choices=levelchoices)
    location = forms.CharField(label="所在地", max_length=128)
    password1 = forms.CharField(label="密码", max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'} ))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # sex = forms.ChoiceField(label='性别', choices=gender)
