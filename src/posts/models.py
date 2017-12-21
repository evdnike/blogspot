from django.db import models
from accounts.models import User

# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length = 255, blank=False, null=False)
    image = models.ImageField(null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    likes = models.IntegerField(default=0)

    class Meta:
        db_table = 'post'
    def __str__(self):
        return self.title

class Comments(models.Model):
    comment = models.TextField(max_length=1024, verbose_name = '')
    comment_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    comment_post = models.ForeignKey(Post)

    class Meta:
        db_table = 'comments'