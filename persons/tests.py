from django.test import TestCase

from .models import Person


class PersonTestCase(TestCase):
    def setUp(self) -> None:
        self.person_1 = Person.objects.create(
            person_name="igor Inokentiev"
        )

    def test_person_creation(self):
        self.assertEqual(
            Person.objects.get(person_name=self.person_1.person_name).person_name,
            "igor Inokentiev"
        )

