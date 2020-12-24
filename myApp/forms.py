import datetime
from django import forms
from django.forms import ModelForm
from .models import ToDo

class AddForm(ModelForm):
    due_date = forms.DateField(initial=datetime.date.today(), widget=forms.SelectDateWidget)
    class Meta:
        model = ToDo
        fields = '__all__'