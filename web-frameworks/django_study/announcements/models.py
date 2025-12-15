from django.db import models
from django.utils import timezone

from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        
        if self.pk:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class User(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        app_label = 'announcements'


class Announcement(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(unique=True)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])    

    class Meta:
        app_label = 'announcements'
