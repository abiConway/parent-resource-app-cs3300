from django import forms
from django.forms import ModelForm
from .models import Group, Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create class for project form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields =('title','service_type', 'price', 'description', 'age_group', 'start_date', 'end_date', 'location')
       #widgets = {
        #    'start_date': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
        #}
        
class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields =('name', 'email', 'phone', 'about')


start_date = forms.DateField(
    widget=forms.DateInput(
        attrs={
            'class' : 'form-control',
            'type' : "date"
        }
    ),
    initial='04-01-2024'

)        

class CreateUserForm(ModelForm):
    class Meta:
        model = Group
        fields =('name', 'email', 'about')



        