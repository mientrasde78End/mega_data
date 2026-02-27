
from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech = models.JSONField()
    repo = models.URLField()
    demo = models.URLField(blank=True, null=True)
    image = CloudinaryField('image', folder='projects', null=True, blank=True)

    def __str__(self):
        return self.title