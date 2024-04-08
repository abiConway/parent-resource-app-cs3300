from django.shortcuts import *
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from .forms import EventForm, CreateUserForm, GroupForm

# Create your views here.

def index(request):
    #I got help from Chat GPT on this function, see comments
    # Get current date and time
    current_datetime = timezone.now()

    # Filter events with end dates in the future __gt is django sytanx for greater than
    #Q is a django object that let's you make complex quieries by combining multiple conditions
    future_events = Event.objects.filter(Q(end_date__gt=current_datetime) | Q(end_date__isnull=True))

    # Pass the filtered events to the template
    return render(request, 'parent_resource_app/index.html', {'future_events': future_events})

def createEvent(request, group_id):
   form = EventForm()
   group = Group.objects.get(pk=group_id)

   if request.method == 'POST':
      #Create a new dictionary with form data and group_id
      event_data = request.POST.copy()
      event_data['group_id'] = group_id
      form = EventForm(event_data)
      if form.is_valid():
         #Save the form without committing to the database
         event = form.save(commit=False)
         #Set the group relationship
         event.group = group
         event.save()

         #redirect back to the group detail page
         return redirect('group-detail', group_id)
   else:
      form = EventForm()


   context = {'form': form }
   return render( request, 'parent_resource_app/event_form.html', context )
   


def updateEvent(request, group_id, event_id):
   event = get_object_or_404(Event, pk=event_id)
   group = event.group

   if request.method == 'POST':
      #Create a new dictionary with form data and group_id
      event_data = request.POST.copy()
      event_data['group_id'] = group_id
      form = EventForm(request.POST, instance=event)
      if form.is_valid():
         #Save the form without committing to the database
         event = form.save(commit=False)
         #Set the group relationship
         event.group = group
         event.save()

         #redirect back to the group detail page
         return redirect('group-detail', group_id)
   else:
      form = EventForm(instance=event)

   context = {'form': form, 'event': event}
   return render(request, 'parent_resource_app/update_event.html', context)



def deleteEvent(request, group_id, event_id):
   event = get_object_or_404(Event, pk=event_id)
    
   
   if request.method == 'POST':
      # Confirming the delete request
      event.delete()
      # Redirect back to the group detail page
      return redirect('group-detail', group_id)

    # If the request method is not POST (e.g., GET), render the confirmation template
   context = {'event': event}
   return render(request, 'parent_resource_app/delete_event.html', context)



def updateGroup(request, group_id):
   group = get_object_or_404(Group, pk=group_id)
   
   if request.method == 'POST':
      #Create a new dictionary with form data and group_id
      group_data = request.POST.copy()
      group_data['group_id'] = group_id
      form = GroupForm(request.POST, instance=group)
      if form.is_valid():
         #Save the form without committing to the database
         group = form.save(commit=False)
         #Set the group relationship
         group.group = group
         group.save()

         #redirect back to the group detail page
         return redirect('group-detail', group_id)
   else:
      form = GroupForm(instance=group)

   context = {'form': form, 'group': group}
   return render(request, 'parent_resource_app/update_group.html', context)



class GroupListView(generic.ListView):
   model = Group

class GroupDetailView(generic.DetailView):
   model = Group

   
class EventListView(generic.ListView):
   model = Event

class EventDetailView(generic.DetailView):
   model = Event