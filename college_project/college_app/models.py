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
    

class Department(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Professor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
