from django.test import TestCase
from django.urls import reverse
from parent_resource_app.forms import *
from django.contrib.auth.models import User

class EventFormTestCase(TestCase):

    def test_valid_form(self):
        data = {'title': 'Test Event', 'description': 'This is a test description for test event.', 'service_type': 'Family Fun', 'price': '25.00', 'age_group': '0y', 'location': 'Test Location', 'start_date': '2024-05-21', 'end_date': '2020-05-31'}
        form = EventForm(data=data)
        self.assertTrue(form.is_valid())

    def test_missing_title_invalid(self):
        data = {'title': '', 'description': 'This is a test description for test event.', 'service_type': 'Family Fun', 'price': '25.00', 'age_group': '0y', 'location': 'Test Location', 'start_date': '2024-05-21', 'end_date': '2020-05-31'}
        form = EventForm(data=data)
        self.assertFalse(form.is_valid() and self.assertIn('title', form.errors)) 