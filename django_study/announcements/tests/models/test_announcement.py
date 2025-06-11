from django.test import TestCase
from announcements.models import Announcement, User


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
    
    def test_announcement_user(self):
        self.assertIsNotNone(self.annoucement.user)

    def test_updated_at_on_save(self):
        # mock
        self.annoucement.title = "Test Updated At"

        #act
        self.annoucement.save()

        # assert
        self.assertIsNotNone(self.annoucement.updated_at)


