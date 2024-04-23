from django.shortcuts import *
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import allowed_users
from tkinter import * 




# Create your views here.

def base_template(request):
   context = { 'redirect_to': request.path }
   return render(request, 'parent_resource_app/base.html', context)


def index(request):
    #I got help from Chat GPT on this querey
    # Get current date and time
    current_date = timezone.now()

    # Filter events with end dates in the future __gt is django sytanx for greater than
    #Q is a django object that let's you make complex quieries by combining multiple conditions
    future_events = Event.objects.filter(Q(end_date__gt=current_date) | Q(end_date__isnull=True))

    # Pass the filtered events to the template
    return render(request, 'parent_resource_app/index.html', {'future_events': future_events})


def login(request):

    # Pass the filtered events to the template
    return render(request, 'registration/login.html')



def logout(request):
    # Pass the filtered events to the template
    return render(request, 'registration/logout.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['organization_role'])
def createEvent(request, organization_id):
   form = EventForm()
   organization = Organization.objects.get(pk=organization_id)

   if request.method == 'POST':
      #Create a new dictionary with form data and organization_id
      event_data = request.POST.copy()
      event_data['organization_id'] = organization_id
      form = EventForm(event_data)
      if form.is_valid():
         start_date = form.cleaned_data['start_date']
         #Save the form without committing to the database
         event = form.save(commit=False)
         #Set the group relationship
         event.organization = organization
         event.save()

         #redirect back to the group detail page
         return redirect('organization-detail', organization_id)
   else:
      form = EventForm()


   context = {'form': form }
   return render( request, 'parent_resource_app/event_form.html', context )
   

@login_required(login_url='login')
@allowed_users(allowed_roles=['organization_role'])
def updateEvent(request, organization_id, event_id):
   event = get_object_or_404(Event, pk=event_id)
   organization = event.organization

   if request.method == 'POST':
      #Create a new dictionary with form data and group_id
      event_data = request.POST.copy()
      event_data['organization_id'] = organization_id
      form = EventForm(request.POST, instance=event)
      if form.is_valid():
         #Save the form without committing to the database
         event = form.save(commit=False)
         #Set the group relationship
         event.organization = organization
         event.save()

         #redirect back to the group detail page
         return redirect('organization-detail', organization_id)
   else:
      form = EventForm(instance=event)

   context = {'form': form, 'event': event}
   return render(request, 'parent_resource_app/update_event.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['organization_role'])
def deleteEvent(request, organization_id, event_id):
   event = get_object_or_404(Event, pk=event_id)
    
   
   if request.method == 'POST':
      # Confirming the delete request
      event.delete()
      # Redirect back to the group detail page
      return redirect('organization-detail', organization_id)

    # If the request method is not POST (e.g., GET), render the confirmation template
   context = {'event': event}
   return render(request, 'parent_resource_app/delete_event.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['organization_role'])
def updateOrganization(request, organization_id):
   organization = get_object_or_404(Organization, pk=organization_id)
   
   if request.method == 'POST':
      #Create a new dictionary with form data and group_id
      organization_data = request.POST.copy()
      organization_data['organization_id'] = organization_id
      form = OrganizationForm(request.POST, instance=organization)
      if form.is_valid():
         #Save the form without committing to the database
         organization = form.save(commit=False)
         #Set the group relationship
         organization.organization = organization
         organization.save()

         #redirect back to the group detail page
         return redirect('organization-detail', organization_id)
   else:
      form = OrganizationForm(instance=organization)

   context = {'form': form, 'organization': organization}
   return render(request, 'parent_resource_app/update_organization.html', context)



def registerPage(request):
   form = CreateUserForm()

   if request.method =='POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         user = form.save()
         username = form.cleaned_data.get('username')
         group = Group.objects.get(name='organization_role')
         user.groups.add(group)
         organization = Organization.objects.create(user=user,)
         organization.save()

         messages.success(request, 'Account was created for ' + username)
         return redirect('login')
      
   context = {'form': form}
   return render(request, 'registration/register.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['organization'])
def userPage(request):
   organization = request.user.organization
   form = OrganizationForm(instance = organization)
   print('organization', organization)
   if request.method == 'POST':
      form = OrganizationForm(request.POST, request.FILES, instance=organization)
      if form.is_vaild():
         form.save()
   context = {'organization': organization, 'form':form}
   return render(request, 'parent_resource_app/user.html', context)




class OrganizationListView(generic.ListView):
   model = Organization

class OrganizationDetailView(generic.DetailView):
   model = Organization

   
class EventListView(generic.ListView):
   model = Event

class EventDetailView(generic.DetailView):
   model = Event