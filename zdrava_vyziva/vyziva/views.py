
from .models import Recept, Autor, DayTime, Coach, Comment, Ingredients
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RecipeGeneratorForm, UserRegistrationForm, CommentForm, ContactForm


def recipe_generator(request):
    if request.method == 'POST':
        form = RecipeGeneratorForm(request.POST)
        if form.is_valid():
            # Implement logic to generate recipes based on daily calories intake
            # For simplicity, let's assume you have a list of recipes
            recipes = Recept.objects.all()[:5]
            return render(request, 'generate_recipes.html', {'recipes': recipes})
    else:
        form = RecipeGeneratorForm()
    return render(request, 'recipe_generator.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('recipe_generator')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_generator')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
