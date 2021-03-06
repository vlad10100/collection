from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20)
    post = models.TextField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title