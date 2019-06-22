from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator


class UserInfoForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=10, validators=[MinLengthValidator(10)], label='Roll No', widget=forms.TextInput(attrs={'placeholder': 'IIITUYYYYY'}))
    class Meta():
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
