from django import forms
from django.forms import ModelForm
from . models import *


class TaskForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'Placeholder': 'Add a task....'}))
    class Meta:
        model = Task
        fields = '__all__'

