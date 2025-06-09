from django.test import TestCase
from announcements.models import Annoucement


class AnnouncementTest(TestCase):
    
    def setUp(self):
        self.annoucement = Annoucement.objects.create(name="Test Model")

    def test_created_at_auto_now_add(self):
        self.assertIsNotNone(self.annoucement.created_at)
        self.assertIsNone(self.annoucement.updated_at)
    
    def test_name(self):
        self.assertEqual(self.annoucement.name,"Test Model")


