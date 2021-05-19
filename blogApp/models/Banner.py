import sys
import uuid
import os
from os.path import splitext

from django.db import models

from blogApp.utils import path_for_banner


class Banner(models.Model):
    name = models.CharField(max_length=32, default="untitled")
    url = models.CharField(max_length=1024, blank=True)
    image = models.ImageField(upload_to=path_for_banner, blank=False)
    is_active = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_banners():
        return Banner.objects.filter(is_active=True)


sys.modules[__name__] = Banner
