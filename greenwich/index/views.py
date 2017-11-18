from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    if request.session['id'] is not None:
        return render(request, 'index/index.html')
    else:
        return redirect('/sign_in/')

def sign_in(request):

    return render(request, 'index/sign_in.html')

def _login(request):
    data = request.POST

    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        request.session['id'] = user.id
        return redirect('/')
    else:
        return redirect('/sign_in/')
