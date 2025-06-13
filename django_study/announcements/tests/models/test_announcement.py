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
    
    def test_announcement_user(self):
        self.assertIsNotNone(self.annoucement.user)

    def test_creat_a_announcement_without_user(self):

        announ = Announcement(
            user=None,
            title="Test Another Announcement",
            description='Test Description.',
            value=decimal.Decimal('2000.01')
        )

        with self.assertRaises(ValidationError) as cm:
            announ.full_clean()

        self.assertIn("user", cm.exception.error_dict)

        expected_error = "This field cannot be null."
        self.assertIn(expected_error, str(cm.exception))

    def test_announcement_fields(self):

        self.assertEqual(self.annoucement.title,"Test Announcement")
        self.assertEqual(self.annoucement.description,"Test Description")
        self.assertEqual(self.annoucement.value, 2000.01)

    def test_announcement_value_exceeds_max_digits(self):

        announ = Announcement(
            user=self.user,
            title="Test Announcement 3",
            description='This description 1.',
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
            title="Test Announcement 2",
            description='Test description.',
            value=decimal.Decimal('1234.567') 
        )

        with self.assertRaises(ValidationError) as cm:
            announ.full_clean()

        self.assertIn("value", cm.exception.error_dict)

        expected_error = "Ensure that there are no more than 2 decimal places."
        self.assertIn(expected_error, str(cm.exception))

    def test_negative_values(self):

        announ = Announcement(
            user=self.user,
            title="Test Announcement 2",
            description='Test description.',
            value=decimal.Decimal('-1234.567') 
        )

        with self.assertRaises(ValidationError) as cm:
            announ.full_clean()

        self.assertIn("value", cm.exception.error_dict)


    def test_for_duplicate_tittles(self):

        announ = Announcement(
            user=self.user,
            title="Test Announcement",
            description='Test Description',
            value=2000.01 
        )

        with self.assertRaises(ValidationError) as cm:
            announ.full_clean()

        self.assertIn("title", cm.exception.error_dict)

        expected_error = 'Announcement with this Title already exists.'
        self.assertIn(expected_error, str(cm.exception))




    def test_updated_at_on_save(self):
        # mock
        self.annoucement.title = "Test Updated At"

        #act
        self.annoucement.save()

        # assert
        self.assertIsNotNone(self.annoucement.updated_at)


