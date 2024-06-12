from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .forms import EmailRegistrationForm,DetailRegistrationForm
from .models import EmailRegister
from django.urls import reverse_lazy




class Index(CreateView):
    form_class = EmailRegistrationForm
    template_name = "nfilili/index.html"
    success_url = "form/"

    def form_valid(self, form):
        self.request.session["email"] = form.cleaned_data['email']
        print(self.request.session['email'])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "success_message" in self.request.session:
            context["success_message"] = self.request.session["success_message"]
            del self.request.session["success_message"] 
            self.request.session.modified = True 
        return context
    
class Form(CreateView):
    
    form_class = DetailRegistrationForm
    template_name = "nfilili/form.html"
    success_url = "/"

    
    def form_valid(self, form):
        email = self.request.session['email']
        email_instance, created = EmailRegister.objects.get_or_create(email=email)
        form.instance.email = email_instance
        response  = super().form_valid(form)
        self.request.session['success_message'] = "Form submitted successfully!"
        self.request.session.modified = True
        return response