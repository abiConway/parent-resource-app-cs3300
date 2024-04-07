from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic

# Create your views here.

def index(request):
    # Render index.html
    return render( request, 'parent_resource_app/index.html')



class GroupListView(generic.ListView):
   model = Group

class GroupDetailView(generic.DetailView):
   model = Group