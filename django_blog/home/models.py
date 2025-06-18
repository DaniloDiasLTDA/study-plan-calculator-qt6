from datetime import datetime

from django.db import models
from django.utils import timezone

from validators.date import year_validator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Year(BaseModel):
    name = models.CharField(
        max_length=4,
        unique=True,
        validators=[year_validator],  # Aplica o validador
        default=datetime.now().year,  # Define o ano atual como valor padrão
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        app_label = 'home'
