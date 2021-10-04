from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=True)
    created_at = models.DateField(auto_created=True, null=True)