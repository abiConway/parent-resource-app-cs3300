from django.forms import ModelForm
from .models import Group, Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create class for project form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields =('title','service_type', 'price', 'description', 'age_group', 'start_date', 'end_date', 'location')
      
        
class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields =('name', 'email', 'phone', 'about')
        

class CreateUserForm(ModelForm):
    class Meta:
        model = Group
        fields =('name', 'email', 'about')



        