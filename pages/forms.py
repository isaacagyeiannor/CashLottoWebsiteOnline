from dataclasses import field
from django import forms
from .models import *
from mainwebsite.models import User
from django.contrib.auth.forms import UserCreationForm

# from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_datepicker_plus.widgets import DatePickerInput

# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields =['name','username', 'email', 'password1', 'password2','country','code','phone_number']
        
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
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
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email 


class BlogForm(forms.ModelForm):
    class Meta:
        model =Blog
        fields ="__all__"
        

class BlogCommentsForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name', "email" ,'body']
        
class TestimonialForm(forms.ModelForm):
    class Meta:
        model =Testimonial
        fields ="__all__"
        
        

class AddDrawForm(forms.ModelForm):
    class Meta:
        model = AddDraw
        fields = ['draw_type', 'date_select', ]
        widgets = {
        'date_select':DatePickerInput()
        }
        
class AddWinDrawForm(forms.ModelForm):
    class Meta:
        model = AddWinDraw
        fields = ['draw_type', 'date_select', 'first_number','second_number','third_number','fourth_number']
        widgets = {
        'date_select':DatePickerInput()
        }
        

class AllDrawForm(forms.ModelForm):
    class Meta:
        model = AllDraw
        fields = '__all__'
        widgets = {
        'date_select':DatePickerInput()
        }