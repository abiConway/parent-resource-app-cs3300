from django.contrib import admin
from parler.admin import TranslatableAdmin

# Register your models here.
from .models import Organization, Event


admin.site.register(Organization, TranslatableAdmin)
admin.site.register(Event, TranslatableAdmin)

