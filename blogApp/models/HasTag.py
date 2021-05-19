import sys

from django.db import models


class HasTag(models.Model):
    post = models.ForeignKey(
        'blogApp.Post', on_delete=models.CASCADE, blank=False, null=False)
    tag = models.ForeignKey(
        'blogApp.Tag', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.post.title} article contains {self.tag.name}"


sys.modules[__name__] = HasTag
