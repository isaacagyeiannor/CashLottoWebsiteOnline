import email
from django import forms
from .models import ForecasterPrediction, UserBase, UserProfile,Stake
from django.contrib.auth.forms import UserCreationForm
from pages.forms import *
from pages.models import *
from django.contrib.auth.forms import (PasswordResetForm,
                                       SetPasswordForm)
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
    
    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))


    class Meta:
        model=UserProfile
        fields= '__all__'  
        exclude= ["user"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True


class PwdResetForm(PasswordResetForm):
    
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        email_ver = UserBase.objects.filter(email=email)
        if not email_ver:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email
    
    class Meta:
        model=UserBase
        fields =[ 'email']
    
class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))
    
    
    # class Meta:
    #     model=UserBase
    #     fields =[ 'email', 'password1', 'password2']

        
# i'll add validation later
class StakeForm(forms.ModelForm):
    class Meta:
        model=Stake
        fields=['game_type','perm_type','first_number','second_number','third_number','fourth_number','fifth_number','payment','winning_amount','price']
        

class ForecasterPredictForm(forms.ModelForm):
    class Meta:
        model = ForecasterPrediction
        fields = ['draw_type', 'date_select', 'first_number','second_number','third_number','fourth_number','fifth_number']
        widgets = {
        'date_select':DatePickerInput()
        }
        