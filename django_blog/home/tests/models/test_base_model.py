from django.test import TestCase
from home.models import BaseModel
from datetime import datetime
from django.utils import timezone


class TestBaseModel(BaseModel):
    pass


class BaseModelTest(TestCase):
    def setUp(self) -> None:
        self._created_at = datetime.now()
        self.test_base_model = TestBaseModel(created_at=self._created_at)

    def test_created_at_auto_now_add(self):
        self.assertIsNotNone(self.test_base_model.created_at)
        self.assertIsNone(self.test_base_model.updated_at)

    def test_updated_at_on_save(self):
        # mock
        self.assertIsNone(self.test_base_model.updated_at)

        # act
        self.test_base_model.updated_at = timezone.now()

        # assert
        self.assertIsNotNone(self.test_base_model.updated_at)
        self.assertEqual(self.test_base_model.created_at, self._created_at)
