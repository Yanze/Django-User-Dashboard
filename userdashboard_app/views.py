from django.shortcuts import render, redirect
# from .models import User
from .form import SignInForm
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth import forms, login, authenticate


class Index(TemplateView):
    template_name = "views/index.html"


def dashboard(request):
    # context = SignInForm.objects.all()
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


class Login(View):
    form = forms.AuthenticationForm
    def get(self, request):
        context = {'form': self.form()}
        return render(request, 'views/login.html', context)

    def post(self, request):
        form = self.form(None, request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'views/login.html', context)
        else:
            return render(request, 'views/login.html', context)
