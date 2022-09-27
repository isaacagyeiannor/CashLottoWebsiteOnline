from django import forms
from .models import ForecasterPrediction, UserBase, UserProfile,Stake
from django.contrib.auth.forms import UserCreationForm
from pages.forms import *
from pages.models import *
from django.contrib.contenttypes.models import ContentType


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model=UserBase
        fields =['name','username', 'email', 'password1', 'password2','country','code','phone_number']
        
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = UserBase.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email   
        
        
class UserProfileForm(forms.ModelForm):
    bio=forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))
    class Meta:
        model=UserProfile
        fields= '__all__'  
        exclude= ["user"]
        