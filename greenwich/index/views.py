from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from index.models import User
from index.forms import UserForm


# Create your views here.
def index(request):

    if 'id' in request.session.keys():
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
    login(request, user)

    if user is not None:
        request.session['id'] = user.id
        return redirect('/')
    else:
        return redirect('/sign_in/')

def logout(request):

    del request.session['id']

    return redirect('/sign_in/')

def create_user(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            # this may be a hack that can be prevented with login
            request.session['id'] = new_user.id
            return redirect('/')
    else:
        form = UserForm()
    
    return render(request, 'index/create_user.html', {'form':form})
