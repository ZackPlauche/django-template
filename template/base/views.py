from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import CreateAccountForm
from .models import *

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard.html')

class CreateAccount(CreateView):
    form_class = CreateAccountForm
    template_name = 'registration/create_account.html'
    success_url = '/'