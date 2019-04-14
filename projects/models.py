from django.db import models

class Project(models.Model):
    # project title
    title = models.CharField(max_length=100)
    # long descripiton
    description = models.TextField()
    # technology tag
    technology = models.CharField(max_length=20)
    # references an image for display
    image = models.FilePathField(path="/img")
