from django.shortcuts import render
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    dict = {}
    return render(request,'index.html',dict)

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        recived = UserCreationForm(request.POST)
        if recived.is_valid():
            recived.save()
            username = recived.cleaned_data['username']
            password = recived.cleaned_data['password1']

            user = authenticate(username = username,password = password)
            login(request,user)
            return HttpResponseRedirect('/homepage')

    dict = {'form' : form}
    return render(request,'user/signup.html',dict)


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')
