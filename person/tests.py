from django.test import TestCase
from .models import Person
from model_mommy import mommy


class PersonTest(TestCase):
    def test_creation(self):
        p1 = mommy.make(Person, name='Test')
        p2 = Person.objects.all()[0]

        self.assertEqual(p1, p2)

    def test_str(self):
        p = mommy.make(Person, name='Test')
        self.assertEqual("Test", p.__str__())