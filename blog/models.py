from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from django_project import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


def user_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.id, filename)

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=user_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)