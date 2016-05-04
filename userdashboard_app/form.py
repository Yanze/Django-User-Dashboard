from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# modify the built-in form
class SignInForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    def save(self, commit=True):
        user = super(SignInForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user
