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
    #path('')

    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    #path('portfolio/<int:portfolio_id>/createProject', views.createProject, name='createEvent'),
    #path('portfolio/<int:portfolio_id>/updateProject/<int:project_id>', views.updateProject, name='updateEvent'),
    #path('portfolio/<int:portfolio_id>/deleteProject/<int:project_id>', views.deleteProject, name='deleteEvent'),
    #path('portfolio/<int:portfolio_id>/updatePortfolio', views.updatePortfolio, name='updateGroup'),
]
