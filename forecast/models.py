from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Mood(models.Model):
    mood_text = models.CharField(max_length=200)
    def __str__(self):
        return self.mood_text
    
    