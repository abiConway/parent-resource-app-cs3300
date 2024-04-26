from django.forms import ModelForm
from .models import Event, Organization
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


#create class for project form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ='__all__'
        exclude = ['organization']

        #Widgets are used to format the form we'll sent to the HTML template. In this case, we're
        #using bootstraps form templates
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'age_group': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-group', 'placeholder': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'class':'form-group', 'placeholder': 'YYYY-MM-DD'}),
        }
    

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields ='__all__'
        exclude = ['user']

        #Widgets are used to format the form we'll sent to the HTML template. In this case, we're
        #using bootstraps form templates
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NO PROFILE INFO, PLEASE UPDATE'}), #class is a bootstrap class
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
        }



#start_date = forms.DateField(
 #   widget=forms.DateInput(
  #      attrs={
   #         'class' : 'form-control',
    #        'type' : "date"
     #   }
    #),
   # initial='04-01-2024'

#)        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']



        