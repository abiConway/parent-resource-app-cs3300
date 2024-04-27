from django.test import TestCase
from django.contrib.auth.models import User
from parent_resource_app.models import Organization, Event

class ModelTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.organization = Organization.objects.create(
            name='Test Organization',
            email='test@example.com',
            phone='555-555-5555',
            about='This is a test about for test organization.',
            user=self.user,
        )
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
    
    def test_organization_creation(self):
        self.assertEqual(self.organization.name, 'Test Organization')
        self.assertEqual(self.organization.email, 'test@example.com')
        self.assertEqual(self.organization.phone, '555-555-5555')
        self.assertEqual(self.organization.about, 'This is a test about for test organization.')
        self.assertEqual(self.organization.user, self.user)
        self.assertEqual(str(self.organization), self.organization.name)
        self.assertEqual(self.organization.get_absolute_url(), '/en/groups/1')

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.service_type, 'Family Fun')
        self.assertEqual(self.event.price, '25.00')
        self.assertEqual(self.event.age_group, '0y')
        self.assertEqual(self.event.description, 'This is a test description for test event.')
        self.assertEqual(self.event.location, 'Test Location')
        self.assertEqual(self.event.start_date, '2024-05-21')
        self.assertEqual(self.event.end_date, '2020-05-31')
        self.assertEqual(self.event.organization, self.organization)
        self.assertEqual(str(self.event), self.event.title)
        self.assertEqual(self.event.get_absolute_url(), '/en/events/1/')
 


 