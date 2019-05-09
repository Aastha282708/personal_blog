from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextFiled()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    author=models.

