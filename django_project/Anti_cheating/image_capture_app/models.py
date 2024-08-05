# models.py

from django.db import models

class cameraStatus(models.Model):
    is_camera = models.BooleanField(default=False)

