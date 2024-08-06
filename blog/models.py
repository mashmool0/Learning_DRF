from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200 , null=True,blank=True)
    Text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title