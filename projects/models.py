from django.db import models


class Project(models.Model):
    rank = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True, max_length=250)
    image = models.ImageField(upload_to="images/")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
