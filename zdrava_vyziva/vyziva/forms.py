from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Recept
from django.contrib.auth.models import User

class CommentForm(forms.Form):
    author = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Pepa z Depa" }))
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":5, "class":"form-control" }))
    rating = forms.IntegerField(required=False, widget=forms.NumberInput(attrs= {"class":"form-control"}))

class ContactForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Evžen" }))
    surname = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Mrkvička" }))
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"evzenmrkvicka@gmail.com" }))
    phone = forms.IntegerField(required=False, widget=forms.NumberInput(attrs= {"class":"form-control", "placeholder":"+420 222 222 222"}))
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":5, "class":"form-control" }))


class RecipeGeneratorForm(forms.Form):
    calories = forms.IntegerField()

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']