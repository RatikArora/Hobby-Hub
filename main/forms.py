from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import post

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        widgets = {
            'username':forms.TextInput(attrs={}),
            'first_name':forms.TextInput(),
            'last_name':forms.TextInput(),
            'email':forms.EmailInput(),
            'password':forms.PasswordInput(attrs={"type":"password","minlength":"5"})
        }


class NewPostForm(forms.ModelForm):
	class Meta:
		model = post
		fields = ['data', 'pic', 'tags']
        
                


from django import forms
from .models import Profile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']