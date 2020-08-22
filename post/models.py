from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    #제목,본문,이미지
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    like = models.ManyToManyField(User, related_name='likes',blank=True)

    def __str__(self):
        return self.title

    def sum(self):
        return self.body[:50]

