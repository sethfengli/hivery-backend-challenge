from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)
    index = models.IntegerField(null=False, primary_key=True)
  
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name