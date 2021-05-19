import sys
import uuid
import os
import re
from os.path import splitext

from django.db import models
from django.contrib.auth.models import User
from authenticationApp import models as Profile_models

from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField
from django_tagify.fields import TagsField

from blogApp.utils import path_for_article_thumbnail

from blogApp.models import HasTag


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    thumbnail = ThumbnailerImageField(
        upload_to=path_for_article_thumbnail, blank=False, resize_source=dict(size=(750, 450), crop=True))
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(
        verbose_name='Code', null=True, blank=True, config_name="default")
    tags = TagsField(max_length=1000, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    like = models.ManyToManyField(User, related_name='blog_likes')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_view_count(self):
        return 1

 
    def get_like_count(self):
        return self.like.count()

    def get_tags(self):
        return HasTag.objects.filter(post__pk=self.pk)

    def get_sample_content(self):
        content = re.sub(r'<[^>]*>', '', self.content)

        return content

    def is_liked(self, user):
        query_set = self.like.all()
        return user in query_set 

    @staticmethod
    def get_posts_by_tag_name(tag_name):
        posts = []
        hasTags = HasTag.objects.filter(tag__name=tag_name)

        for hasTag in hasTags:
            posts.append(hasTag.post)

        return posts

    @staticmethod
    def get_author_profile_by_author(author):
        return Profile_models.Profile.get_profile_by_user(author)

    @staticmethod
    def get_posts():
        return Post.objects.filter(public=True)

    @staticmethod
    def get_post_by_id(pk):
        return Post.objects.get(id=pk)



sys.modules[__name__] = Post
