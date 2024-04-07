from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.utils import timezone
from django.db.models import Q

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


class GroupListView(generic.ListView):
   model = Group

class GroupDetailView(generic.DetailView):
   model = Group