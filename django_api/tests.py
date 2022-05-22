
from django.test import TestCase
from .models import Thing

class ThingTests(TestCase):

    # just setting up the data
    @classmethod
    def setUpTestData(cls):
        testting = Thing.objects.create(title = 'test_thing', describtion= 'Testing thing')
        testting.save()

    def test_things_model(self):
        thing = Thing.objects.get(id = 1)
        actual_title = thing.title
        self.assertEqual(actual_title, 'test_thing')

