import sys

from django.db import models
from django.contrib.auth.models import User

from blogApp.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)


sys.modules[__name__] = Comment
