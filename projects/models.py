from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    url = models.URLField(max_length=250)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.title}"
