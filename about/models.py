from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", default="images/image-not-found.jpg")

    def __str__(self):
        return f"{self.title}, {self.created_on}"
