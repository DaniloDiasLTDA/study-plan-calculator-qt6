from django.test import TestCase
from announcements.models import User
from django.core.exceptions import ValidationError


class UserTest(TestCase):
    
    def setUp(self):

        self.user = User.objects.create(
            name="Test Name",
            email='test@email.test',
            password='test2'
        )

        self.user.full_clean()
    
    def test_created_at_auto_now_add(self):
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNone(self.user.updated_at)

    def test_updated_at_on_save(self):
        # mock
        self.user.title = "Test Updated At"

        #act
        self.user.save()

        # assert
        self.assertIsNotNone(self.user.updated_at)

    def test_user(self):
        self.assertEqual(self.user.name, 'Test Name')
        self.assertEqual(self.user.email, 'test@email.test')
        self.assertEqual(self.user.password, 'test2')

    def test_name_invalid_max_length(self):
        self.user.name = 'a' * 101

        with self.assertRaises(ValidationError) as cm:
            self.user.full_clean()
      
        self.assertIn("Ensure this value has at most 100 characters", str(cm.exception))
        self.assertIn("name", cm.exception.error_dict)

    def test_max_length_password(self):
        self.user.password = 'a' * 51

        with self.assertRaises(ValidationError) as cm:
            self.user.full_clean()
        
        self.assertIn('Ensure this value has at most 50 characters', str(cm.exception))
        self.assertIn('password', cm.exception.error_dict)
    
    def test_email_field_rejects_invalid_format_on_full_clean(self):

        user = User(
            name="Test Name",
            email="Test Email",
            password="test_password"
        )

        with self.assertRaises(ValidationError) as cm:
            user.full_clean() 

        self.assertIn("Enter a valid email address.", str(cm.exception))
        self.assertIn("email", cm.exception.error_dict)

    def test_unique_email_creation(self):

        user = User(
            name="testuser2",
            email="test@email.test", 
            password='1223'
        )

        with self.assertRaises(ValidationError) as cm:
            user.full_clean()
    
        expected_error = 'User with this Email already exists.'
        self.assertIn(expected_error, str(cm.exception))
