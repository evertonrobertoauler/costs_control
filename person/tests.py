from django.test import TestCase
from .models import Person


class PersonTest(TestCase):
    def test_creation(self):
        p1 = Person(name='Test', institution='Test')
        p1.save()

        p2 = Person.objects.all()[0]

        self.assertEqual(p1, p2)

    def test_str(self):
        p = Person(name='Test')
        self.assertEqual("Test", p.__str__())