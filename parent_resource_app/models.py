from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField


# Create your models here.

class Group(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField("Email", max_length=200, unique=True)
    phone = models.CharField(max_length= 20, null=True)
    about = models.CharField(max_length=200)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('group-detail', args=[str(self.id)])



class Event(models.Model):
    #List of choices for major value in database, human readable name
    SERVICES = (
    ('Fam-Fun', 'Family Fun'),  
    ('Health', 'Health and Well-being'),
    ('Finance', 'Benefits or Financial Aid'),
    )


    AGEGROUP = (
        ('0', '0-1 years'),
        ('1', '1-2 years'),
        ('2', '2-3 years'),
        ('3', '3-4 years'),
        ('4', '4-5 years'),
        ('5', '5-6 years'),
        ('6', '6-7 years'),
        ('7', '7-8 years'),
        ('8', '8-9 years'),
        ('9', '9-10 years'),
        ('10', '10-11 years'),
        ('11', '11-12 years'),
        ('12', '12-13 years'),
        ('13', '13-14 years'),
        ('14', '14-15 years'),
        ('15', '15-16 years'),
        ('16+', '16 or older'),
        ('P', 'For Parents'),
        ('All', 'All ages'),
    )

    title = models.CharField(max_length=200)
    age_group = MultiSelectField(choices=AGEGROUP, max_length=3)
    service_type = models.CharField("Type of Event", max_length=200, choices=SERVICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField("Start Date", auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateTimeField("End Date", auto_now=False, auto_now_add=False, null=True)
    location = models.CharField("Location", max_length=200, null = True)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=None)


    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])