from django import forms
from django.utils import timezone
from .models import (profile, data)
from django.contrib.auth import authenticate
import os
from django.core.exceptions import ValidationError
from froala_editor.widgets import FroalaEditor

position_choices = (
    ("intern", "intern"),
    ("staff", "staff"),
)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=32, widget=forms.TextInput())
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())

    def clean(self):
        super(UserLoginForm, self).clean()
        try:
            u_name, pwd = self.cleaned_data["username"], \
                          self.cleaned_data["password"]
            user = authenticate(username=u_name, password=pwd)
        except Exception:
            raise forms.ValidationError \
                ("Username and/or Password is not entered")
        if not user:
            raise forms.ValidationError("Invalid username/password")
        return user


class AddForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    topic = forms.CharField()


class add_data(forms.ModelForm):
    subtopic=forms.CharField
    content = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = data
        fields = ('subtopic', 'content')