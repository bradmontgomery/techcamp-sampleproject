from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    content = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
