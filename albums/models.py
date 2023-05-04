from django.db import models
from django.utils import timezone

class Album(models.Model):
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=255, default='New Album')
    creation_datetime = models.DateTimeField(default=timezone.now)
    release_datetime = models.DateTimeField(default=timezone.now)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
