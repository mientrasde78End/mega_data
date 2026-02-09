
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech = models.JSONField()
    repo = models.URLField()
    demo = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/", null=True)

    def __str__(self):
        return self.title