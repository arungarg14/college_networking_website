from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator
from application.models import Profile


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


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta():
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        widgets = {
            'Hobbies': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'Skills' : forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Write in brief. It would help others to find you'}),
            'Linkedin_URL' : forms.TextInput(attrs={'placeholder': 'https://www.linkedin.com/.......','size':'50'}),
        }
        fields = ['Name','Branch','Linkedin_URL','Hobbies','Skills','Contact_NO','image']
