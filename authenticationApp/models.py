import uuid
import os
from os.path import splitext

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from easy_thumbnails.fields import ThumbnailerImageField

from blogApp.models import Post
from blogApp.utils import path_for_profile_pic


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepic = ThumbnailerImageField(
        upload_to=path_for_profile_pic, blank=False, resize_source=dict(size=(240, 240), crop=True))
    firstname = models.CharField(max_length=20, blank=True, default="")
    lastname = models.CharField(max_length=20, blank=True, default="")
    phone = models.CharField(max_length=20, blank=True, default="")
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)

    def get_articles(self, include_private=False):
        if include_private:
            return Post.objects.filter(author=self.user)

        return Post.objects.filter(author=self.user, public=True)

    @staticmethod
    def get_profile_by_user(user):
        profile = Profile.objects.get(user=user)

        return profile

    @staticmethod
    def get_profile_by_username(username):
        profile = Profile.objects.get(user__username=username)

        return profile

    @staticmethod
    def verify_profile_by_user(user):
        profile = Profile.get_profile_by_user(user)

        profile.is_verified = True
        profile.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
