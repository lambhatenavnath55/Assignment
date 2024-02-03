from django.db import models
from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    established = models.IntegerField()
    description = models.TextField()
    website = models.URLField(max_length=200, blank=True)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name
