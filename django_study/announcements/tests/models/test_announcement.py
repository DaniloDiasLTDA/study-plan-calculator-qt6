import decimal

from django.test import TestCase
from announcements.models import Announcement, User
from django.core.exceptions import ValidationError


class AnnouncementTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test Name",
            email='Test@email.text',
            password='test2'
        )
        self.user.full_clean()

        self.annoucement = Announcement.objects.create(
            user=self.user,
            title="Test Announcement",
            description='Test Description',
            value=2000.01
        )

    def test_created_at_auto_now_add(self):
        self.assertIsNotNone(self.annoucement.created_at)
        self.assertIsNone(self.annoucement.updated_at)

    def test_announcement(self):
        self.assertEqual(self.annoucement.title,"Test Announcement")
        self.assertEqual(self.annoucement.description,"Test Description")
        self.assertEqual(self.annoucement.value, 2000.01)

    def test_announcement_value_exceeds_max_digits(self):

        announ = Announcement(
            user=self.user,
            title="Test Announcement - Invalid Max Digits",
            description='This description is for a max digits test.',
            value=decimal.Decimal('1234567890.12')
        )

        with self.assertRaises(ValidationError) as cm:
            announ.full_clean()

        self.assertIn("value", cm.exception.error_dict)
        expected_error = "Ensure that there are no more than 10 digits in total."
        self.assertIn(expected_error, str(cm.exception))


    def test_announcement_value_exceeds_decimal_places(self):

        announ = Announcement(
            user=self.user,
            title="Test Announcement - Invalid Decimal Value",
            description='This description is for an invalid value test.',
            value=decimal.Decimal('1234.567') # Value with 3 decimal places
        )

        with self.assertRaises(ValidationError) as cm:
            announ.full_clean()

        self.assertIn("value", cm.exception.error_dict)

        expected_error = "Ensure that there are no more than 2 decimal places."
        self.assertIn(expected_error, str(cm.exception))

    def test_announcement_user(self):
        self.assertIsNotNone(self.annoucement.user)

    def test_updated_at_on_save(self):
        # mock
        self.annoucement.title = "Test Updated At"

        #act
        self.annoucement.save()

        # assert
        self.assertIsNotNone(self.annoucement.updated_at)


