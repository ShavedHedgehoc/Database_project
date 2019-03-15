from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth

from .forms import MyForm
# Create your views here.

def test(request):
    context={}
    if request.method=="POST":
        form=MyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form=MyForm()
    context={"form":form}
    return render(request, 'test.html', context)

def login(request):
    context={}
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            login_error="Проверьте имя пользователя и пароль"
            context={"login_error":login_error}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)
    


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
