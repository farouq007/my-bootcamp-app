from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=30, 
							   widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	password = forms.CharField(label="Password", max_length=30, 
							   widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class SignUpForm(UserCreationForm):
	first_name= forms.CharField(max_length=150,
		widget=forms.TextInput(
			attrs={'class':'form-control', 'type':'text', 'id':'first_name' , 'placeholder':'Name',
			'autofocus':'autofocus'}))
	last_name= forms.CharField(max_length=150,
		widget=forms.TextInput(
			attrs={'class':'form-control', 'type':'text', 'id':'last_name', 'placeholder':'Surname'}))
	username = forms.CharField(max_length=150,
		widget=forms.TextInput(
			attrs={'class':'form-control', 'type':'text', 'id':'username', 'placeholder':'Username'}))
	password1  = forms.CharField(max_length=150,
		widget=forms.PasswordInput(
			attrs={'class':'form-control',  'id':'password1', 'placeholder':'password'}))
	password2  = forms.CharField(max_length=150,
		widget=forms.PasswordInput(
			attrs={'class':'form-control',  'id':'password2', 'placeholder':'password'}))
	email  = forms.EmailField(max_length=150,
		widget=forms.TextInput(
			attrs={'class':'form-control', 'type':'email', 'id':'e_mail', 'placeholder':'e.g john@gmail.com'}))
	address= forms.CharField(max_length=150,
		widget=forms.TextInput(
			attrs={'class':'form-control', 'type':'text', 'id':'address', 'placeholder':'address'}))
	class Meta:
	    model = User
	    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','address',)

class MyForm(forms.Form):
	title= forms.CharField(
		widget=forms.TextInput(
			attrs={'class':'form-control',  'type':'text'}))
	text= forms.CharField(
		widget=forms.TextInput(
			attrs={'class':'form-control', 'style':'height:100px;', 'type':'text'}))
	

class FeedsForm(forms.Form):
	text= forms.CharField(
		widget=forms.TextInput(
			attrs={'class':'form-control', 'style':'height:100px;', 'type':'text'}))
