from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
#from django.forms import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
 

# Create your models here.

class Organization(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(_('about'), max_length=200)

    name = models.CharField(_('Name'), max_length=200)
    email = models.EmailField(_('Email'), max_length=200)
    phone = models.CharField(_('Phone'), max_length= 20, null=True)
    #@receiver(post_save, sender=User)
    #def create_user_organization(sender, instance, created, **kwargs):
    #    if created:
    #   Organization.objects.create(user=instance)

    #@receiver(post_save, sender=User)
    #def save_user_organization(sender, instance, **kwargs):
    # print("save",sender, instance,**kwargs)
    #instance.organization.save()

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('organization-detail', args=[str(self.id)])



class Event(models.Model):
    #List of choices for major value in database, human readable name
    SERVICES = (
    ('Family Fun', _('Family Fun')),  
    ('Health and Well-being', _('Health and Well-being')),
    ('Benefits or Financial Aid', _('Benefits or Financial Aid')),
    )

    #The left must include text value, not just number
    AGEGROUP = (
        ('0y', _('0-1 years')),
        ('1y', _('1-2 years')),
        ('2y', _('2-3 years')),
        ('3y', _('3-4 years')),
        ('4y', _('4-5 years')),
        ('5y', _('5-6 years')),
        ('6y', _('6-7 years')),
        ('7y', _('7-8 years')),
        ('8y', _('8-9 years')),
        ('9y', _('9-10 years')),
        ('10y', _('10-11 years')),
        ('11y', _('11-12 years')),
        ('12y', _('12-13 year')),
        ('13+', _('13 or older')),
        ('P', _('For Parents')),
        ('All', _('All ages')),
    )

 
    title = models.CharField(_('Title'), max_length=200)
    service_type = models.CharField(_("Type of Event"), max_length=200, choices=SERVICES)

    description = models.TextField(_('Description'), max_length=200)
    age_group = MultiSelectField(_('Age Group'), choices=AGEGROUP, max_length=25)

    location = models.CharField(_('Location'), max_length=200, null = True, blank=True)

    start_date = models.DateField(_('Start Date'), auto_now=False, auto_now_add=False, null=True, blank=True)
    end_date = models.DateField(_('End Date'), auto_now=False, auto_now_add=False, null=True, blank=True)
    price = models.DecimalField(_('Price'), max_digits=5, decimal_places=2)

    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None)


    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])