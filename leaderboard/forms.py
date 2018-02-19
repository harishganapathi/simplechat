from django import forms 
from .models import Scorecard
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Enter_Score(forms.ModelForm):
    class Meta:
        model = Scorecard
        fields = ('name','score')


