# accounts/views.py
from django.shortcuts import render
from .forms import CreateCustomUser
from django.views import generic


class Register(generic.CreateView):
    form_class = CreateCustomUser
    success_url = 'login'
    template_name = 'signup.html'
