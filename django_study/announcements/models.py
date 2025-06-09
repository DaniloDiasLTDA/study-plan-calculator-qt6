from django.db import models
from django.utils import timezone


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        
        if self.pk:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    

class Annoucement(BaseModel):
    name = models.CharField(max_length=100)
    

    class Meta:
        app_label = 'announcements' # 
