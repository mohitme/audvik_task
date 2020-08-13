from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
# Create your models here.

class csv_file(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=settings.MEDIA_ROOT, validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)