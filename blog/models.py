from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    Text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlockUser(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

