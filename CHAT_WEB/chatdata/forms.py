from django import forms
from django.forms import ModelForm
from .models import message

class messageForm(forms.ModelForm):

    class Meta():
        model = message
        fields = ['mesg']
