from django.contrib import admin

# Register your models here.
from .models import Group, Event

admin.site.register(Group)
admin.site.register(Event)

