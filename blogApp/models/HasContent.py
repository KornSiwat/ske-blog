import sys

from django.db import models


class HasContent(models.Model):
    content_section = models.ForeignKey(
        'blogApp.ContentSection', on_delete=models.CASCADE, blank=False, null=False)
    content = models.ForeignKey(
        'blogApp.Post', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.content_section.name} Section contains {self.content.title}"


sys.modules[__name__] = HasContent
