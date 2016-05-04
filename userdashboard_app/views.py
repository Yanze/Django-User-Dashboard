from django.shortcuts import render, redirect
from .models import User
from .form import SignInForm
from django.views.generic import View, TemplateView
from django.contrib.auth import forms

class Index(TemplateView):
    template_name = "views/index.html"

def dashboard(request):
    return render(request, 'views/dashboard.html')

class Signin(View):
    form = SignInForm
    def get(self, request):
        context = {'form': self.form()}
        return render(request, 'views/signin.html', context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return redirect('signin')
