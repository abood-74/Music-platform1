from django.db import models

class Artist(models.Model):
    
    stage_name = models.CharField(unique = True, blank = False,)
    social_link = models.URLField(blank = True,)
    
    def __str__(self) -> str:
        return self.stage_name
    
    class Meta:
        ordering = ['stage_name']
        
