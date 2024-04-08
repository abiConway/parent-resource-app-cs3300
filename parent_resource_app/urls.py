from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('groups/', views.GroupListView.as_view(), name='groups'),
    path('groups/<int:pk>', views.GroupDetailView.as_view(), name='group-detail'),
    
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('group/<int:group_id>/createEvent', views.createEvent, name='createEvent'),
    path('group/<int:group_id>/updateEvent/<int:event_id>', views.updateEvent, name='updateEvent'),
    path('group/<int:group_id>/deleteEvent/<int:event_id>', views.deleteEvent, name='deleteEvent'),
    path('group/<int:group_id>/updateGroup', views.updateGroup, name='updateGroup'),
]
