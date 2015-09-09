from django.test import TestCase

from .models import Character

# Create your tests here.


class CharacterNameTestCase(TestCase):
    def setUp(self):
        Character.objects.create(first_name='Karl', last_name='Käfer', user=None)

    def test_name_format_correct(self):
        karl = Character.objects.get(first_name='Karl')
        self.assertEqual('Karl Käfer', karl.__str__())

    def test_default_complete_name(self):
        obj = Character.objects.create(user=None)
        self.assertEqual('unnamed unnamed', obj.__str__())

    def test_default_first_name(self):
        obj = Character.objects.create(last_name='placeholder', user=None)
        self.assertEqual('unnamed placeholder', obj.__str__())

    def test_default_last_name(self):
        obj = Character.objects.create(first_name='placeholder', user=None)
        self.assertEqual('placeholder unnamed', obj.__str__())

