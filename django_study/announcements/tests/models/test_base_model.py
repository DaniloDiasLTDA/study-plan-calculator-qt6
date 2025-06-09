from django.test import TestCase
from announcements.models import BaseModel

class BaseModelTest(TestCase):
    def setUp(self):
       self.base_model = BaseModel.objects.create()

    def test_created_at_auto_now_add(self):
        self.assertIsNotNone(self.base_model)
