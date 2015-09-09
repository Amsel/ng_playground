from django.test import TestCase

from .models import Character

# Create your tests here.


class CharacterTestCase(TestCase):
    def setUp(self):
        Character.objects.create(first_name='Karl', last_name='Käfer', user=None)

    def test_name_format_correct(self):
        karl = Character.objects.get(first_name='Karl')
        self.assertEqual('Karl Käfer', karl.__str__())
