from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # date_posted = models.DateTimeField(default=timezome.now)
    date_posted = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user deleted, delete post too

    def __str__(self):
        return self.title
