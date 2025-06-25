from django.core.exceptions import ValidationError
from django.test import TestCase

from home.models import Year
from validators.date import YEAR_VALIDATOR_MESSAGE


class YearTest(TestCase):
    def setUp(self) -> None:
        self.year = Year.objects.create(name='2026')

    def test_update_model(self) -> None:
        # mock
        self.year.name = '2099'

        # act
        self.year.save()

        # assert
        self.assertIsNotNone(self.year.updated_at)
        self.assertEqual(self.year.name, '2099')

    def test_max_length(self) -> None:
        self.year.name = 'a' * 100

        with self.assertRaises(ValidationError) as cm:
            self.year.full_clean()

        self.assertIn(YEAR_VALIDATOR_MESSAGE, str(cm.exception))
        self.assertIn('name', cm.exception.error_dict)

    def test_unique_validator(self) -> None:
        duplicate_year = Year(name='2026')

        with self.assertRaises(ValidationError) as cm:
            duplicate_year.full_clean()

        self.assertIn('Year with this Name already exists.', cm.exception.message_dict['name'])

    def test_name_validator(self) -> None:
        self.year.name = '2026Q.2'

        with self.assertRaises(ValidationError) as cm:
            self.year.full_clean()

        self.assertIn(YEAR_VALIDATOR_MESSAGE, cm.exception.message_dict['name'])
