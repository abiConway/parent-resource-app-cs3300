from django.urls import path, include
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('groups/', views.OrganizationListView.as_view(), name='organizations'),
    path('groups/<int:pk>', views.OrganizationDetailView.as_view(), name='organization-detail'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('group/<int:organization_id>/createEvent', views.createEvent, name='createEvent'),
    path('group/<int:organization_id>/updateEvent/<int:event_id>', views.updateEvent, name='updateEvent'),
    path('group/<int:organization_id>/deleteEvent/<int:event_id>', views.deleteEvent, name='deleteEvent'),
    path('group/<int:organization_id>/updateGroup', views.updateOrganization, name='updateOrganization'),
    #path('group/createGroup', views.createOrganization, name='createOrganization'),


    #user accounts
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/register', views.registerPage, name = 'register-page'),
    path('accounts/login', views.login, name='login-page'),
    path('accounts/logout', views.logout, name='logout-page'),
    path('user/', views.userPage, name='user_page'),

    #translation
    path('i18n/', include('django.conf.urls.i18n')),

]
