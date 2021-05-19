import sys

from django.db import models

from blogApp.models import Post
from blogApp.models import HasContent
from blogApp.models import Tag


class ContentSection(models.Model):
    TAG = "Tag"
    LATEST = "Latest"
    CUSTOM = "Custom"
    ALL = "All"
    CONTENT_SOURCE = [
        (ALL, ALL),
        (TAG, TAG),
        (CUSTOM, CUSTOM)
    ]

    TITLE = "Title"
    OLDEST = "Oldest"
    NEWEST = "Newest"
    VIEW = "View"
    LIKE = "Like"
    SORT_BY = [
        (TITLE, TITLE),
        (OLDEST, OLDEST),
        (NEWEST, NEWEST),
        (VIEW, VIEW),
        (LIKE, LIKE)
    ]

    MAX_SIZE = 32
    SIZES = zip(range(1, MAX_SIZE), range(1, MAX_SIZE))

    MAX_ORDER = 16
    ORDERS = zip(range(1, MAX_ORDER), range(1, MAX_ORDER))

    name = models.CharField(max_length=32, default="untitled section")
    content_source = models.CharField(
        max_length=32,
        choices=CONTENT_SOURCE,
        default=TAG,
    )
    sort_by = models.CharField(
        max_length=32,
        choices=SORT_BY,
        default=TITLE,
    )
    size = models.IntegerField(choices=SIZES, default=1)
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE,  blank=True, null=True)
    section_order = models.IntegerField(choices=ORDERS, default=1)
    is_active = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.name

    def get_contents(self):
        contents = []
        source = self.content_source
        sort_by = self.sort_by

        if source == ContentSection.TAG:
            contents = self.get_tag_contents()
        elif source == ContentSection.CUSTOM:
            contents = self.get_custom_contents()
        elif source == ContentSection.ALL:
            contents = Post.get_posts()

        contents = list(contents)

        if sort_by == ContentSection.TITLE:
            contents.sort(key=lambda content: content.title)
        elif sort_by == ContentSection.OLDEST:
            contents.sort(key=lambda content: content.created_on)
        elif sort_by == ContentSection.NEWEST:
            contents.sort(
                key=lambda content: content.created_on, reverse=True)
        elif sort_by == ContentSection.VIEW:
            contents.sort(
                key=lambda content: content.get_view_count(), reverse=True)
        elif sort_by == ContentSection.LIKE:
            contents.sort(
                key=lambda content: content.get_like_count(), reverse=True)

        contents = contents[:self.size]

        return contents

    def get_tag_contents(self):
        return Post.objects.filter(tag__name__in=[self.tag.name])

    def get_custom_contents(self):
        custom_contents = []
        has_contents = HasContent.objects.filter(
            content_section=self)

        for has_content in has_contents:
            custom_contents.append(has_content.content)

        return custom_contents

    @staticmethod
    def get_content_sections():
        return ContentSection.objects.filter(is_active=True)

    




sys.modules[__name__] = ContentSection
