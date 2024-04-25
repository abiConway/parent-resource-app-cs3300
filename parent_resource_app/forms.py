from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from parler.forms import TranslatableModelForm

#create class for project form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ='__all__'
        exclude =['organization']
        TranslatedFields = '__all__'

       #widgets = {
        #    'start_date': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
        #}
        
class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields ='__all__'
        exclude =['user']
        TranslatedFields = ['about']


start_date = forms.DateField(
    widget=forms.DateInput(
        attrs={
            'class' : 'form-control',
            'type' : "date"
        }
    ),
    initial='04-01-2024'

)        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']



        