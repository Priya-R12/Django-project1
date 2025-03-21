from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    post_title = models.CharField(max_length=255,default="")
    post_image = models.ImageField(default=0)
    post_id = models.IntegerField(default=0)
    post_at = models.DateTimeField(default=now)
    