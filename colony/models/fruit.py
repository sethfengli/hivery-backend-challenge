from django.db import models

class Fruit(models.Model):
    index = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
   
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        