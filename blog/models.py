from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)#auto_now=True auto_now_add=True
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title