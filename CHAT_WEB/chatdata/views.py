from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .forms import messageForm
from .models import message
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    users = User.objects.all()
    mainuser = request.user
    dict = {'users' : users,'mainuser' : mainuser}
    return render(request,'chatdata/homepage.html',dict)

@login_required
def chatpage(request,reciver_id):
    reciver = get_object_or_404(User, id=reciver_id)

    form = messageForm()

    sendername = request.user.username
    recivername = reciver.username

    mesgs = []
    allmesgs = message.objects.all()
    for mesg in allmesgs:
        if mesg.sender == sendername and mesg.reciver == recivername:
            mesgs.append(mesg)
        if mesg.sender == recivername and mesg.reciver == sendername:
            mesgs.append(mesg)


    dict = {'form':form,'reciver' : reciver,"mesgs" : mesgs}
    return render(request,'chatdata/chatpage.html',dict)

@login_required
def savemesg(request,reciver_id):
    reciver = get_object_or_404(User, id=reciver_id)
    sender  = request.user
    form= messageForm(request.POST)
    if form.is_valid():
        mesg = form.cleaned_data['mesg']
        mesgobject = message.objects.create(mesg = mesg,sender = sender.username,reciver = reciver.username)
        mesgobject.save()
    return chatpage(request, reciver_id)
