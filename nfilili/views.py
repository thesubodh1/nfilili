from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .forms import EmailRegistrationForm,DetailRegistrationForm
from .models import EmailRegister



class Index(CreateView):
    form_class = EmailRegistrationForm
    template_name = "nfilili/index.html"
    success_url = "form/"

    def form_valid(self, form):
        self.request.session["email"] = form.cleaned_data['email']
        print(self.request.session['email'])
        return super().form_valid(form)
    

class Form(CreateView):
    form_class = DetailRegistrationForm
    template_name = "nfilili/form.html"
    success_url = "success/"
    
    def form_valid(self, form):
        email = self.request.session['email']
        email_instance, created = EmailRegister.objects.get_or_create(email=email)
        form.instance.email = email_instance
        return super().form_valid(form)
    

class success(TemplateView):
    template_name = "nfilili/success.html"
    