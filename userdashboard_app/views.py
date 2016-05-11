from django.shortcuts import render, redirect
from .form import SignInForm
from django.views.generic import View, TemplateView, ListView, UpdateView, RedirectView
from django.contrib.auth import forms, login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



class Index(TemplateView):
    template_name = "views/index.html"

# login_required() takes one optional parameter: redirect_field_name
# login_required() also takes an optional parameter: login_url
@login_required(login_url="signin")
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("signin")
    users = User.objects.all()
    return render(request, 'views/dashboard.html', {'users': users})

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
        context = {'form': self.form}
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

def logout_view(request):
    logout(request)
    return redirect("signin")



"""
TO DO LIST
questions:
- j'arrive pas clear input after submition
- j'arrive pas log out, apres avoir logged out, quand get dashboad page, user est
toujours logged in
- decorators ???

1. get all users to display on the dashboad page
2. forgot password, allows user to reset password
3. edit and delete user
4. user login as admin, manager, general user(has different access)
5. admin has all access and rights, can assign manager
6. manager can only manage posts(add/delete/update post), delete user
7. user can send private message to everyone

"""
