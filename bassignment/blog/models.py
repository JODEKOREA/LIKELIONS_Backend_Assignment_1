from pickle import TRUE
from django.db import models
from django.conf import settings
from account.models import CustomUser

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=10)
    pub_date = models.DateTimeField()
    body = models.TextField(null=TRUE)
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:150]

class Comment(models.Model):
    post = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank = True, on_delete = models.CASCADE)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content