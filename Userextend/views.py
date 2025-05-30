from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from Userextend.forms import SignUpForm, LoginForm


class UserCreateView(CreateView):
    template_name = 'Userextend/register.html'
    model = User
    form_class = SignUpForm
    success_url = '/user_login/'

class UserLoginView(LoginView):
    template_name = 'Userextend/login.html'
    form_class = LoginForm
    success_url = '/'

