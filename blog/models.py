from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    image = models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def snippet(self):
        return  self.content[:100] + '...'