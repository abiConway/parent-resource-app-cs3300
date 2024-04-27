from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from parent_resource_app.models import Organization, Event

class ViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username='testuser', password='testpassword')

        # Create a test organization
        self.organization = Organization.objects.create(
            name='Test Organization',
            email='test@example.com',
            phone='555-555-5555',
            about='This is a test about for test organization.',
            user=self.user,
        )
        
        # Create a test event
        self.event = Event.objects.create(
            title='Test Event',
            service_type='Family Fun',
            price='25.00',
            age_group='0y',
            description='This is a test description for test event.',
            location='Test Location',
            start_date='2024-05-21',
            end_date='2020-05-31',
            organization=self.organization,
        )
    
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parent_resource_app/index.html')

    def test_create_event_view(self):
        client = Client()
        response = client.get(reverse('createEvent', kwargs={'organization_id': self.organization.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parent_resource_app/event_form.html')

        # Test POST request
        data = {
            'title': 'Test Event 2',
            'description': 'This is a test description for test event 2.',
            'service_type': 'Family Fun',
            'price': '25.00',
            'age_group': '0y',
            'location': 'Test Location',
            'start_date': '2024-05-21',
            'end_date': '2020-05-31'
        }
        response = client.post(reverse('createEvent', kwargs={'organization_id': self.organization.id}), data=data)
        self.assertEqual(response.status_code, 302)

        # Check if the event was actually created
        event_count = Event.objects.filter(organization=self.organization).count()
        self.assertEqual(event_count, 2)  # Assuming there was already one event created in the setup()

    def test_create_event_view_invalid_form(self):
        client = Client()
        response = client.get(reverse('createEvent', kwargs={'organization_id': self.organization.id}), {})
        self.assertEqual(response.status_code, 200)  # Expecting the form to be rendered
        self.assertContains(response, 'This field is required.')  # Expecting the form error messages
