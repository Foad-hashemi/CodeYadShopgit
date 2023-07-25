from django.shortcuts import render
from django.views.generic import View, FormView
from django import forms
from django.forms.utils import ValidationError
from .forms import RegisterForm


class Register(FormView):
    template_name = 'Accounts/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
