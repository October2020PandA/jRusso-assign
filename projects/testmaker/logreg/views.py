from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    if 'login_id' in request.session:
        return redirect('/home/')
    context = {
        'title': 'Test Maker App - Welcome',
    }
    return render(request, 'logreg.html', context)

def register(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    hashed_pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email_address'],  pw=hashed_pw)
    request.session['login_id'] = User.objects.get(email=request.POST['email_address']).id
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    user = User.objects.get(email=request.POST['email_address_lg'])
    request.session['login_id'] = user.id
    return redirect('/')

def logout(request):
    if 'login_id' in request.session:
        del request.session['login_id']
    return redirect('/')