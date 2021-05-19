import sys

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


from blogApp.models import HasTag
from blogApp.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=1000, default="untitled", unique=True)

    def __str__(self):
        return self.name

    def get_tagged_posts(self):
        return HasTag.objects.filter(tag__name=self.name)

    @staticmethod
    def get_tags():
        tags = list(Tag.objects.all().order_by('name'))

        for tag in tags:
            if len(tag.get_tagged_posts()) == 0:
                tags.remove(tag)

        return tags


@receiver(post_save, sender=Post)
def create_new_post(sender, instance, created, **kwargs):
    if created:
        comma_separated_tags = str(instance.tags).split(",")
        comma_separated_tags = [
            slugify(tag, allow_unicode=True) for tag in comma_separated_tags]

        for tag_name in comma_separated_tags:
            tag, is_success = Tag.objects.update_or_create(
                name=tag_name, defaults={'name': tag_name})
            HasTag.objects.create(post=instance, tag=tag)


@receiver(post_save, sender=Post)
def edit_post(sender, instance, **kwargs):
    for hasTagObject in HasTag.objects.filter(post=instance):
        hasTagObject.delete()

    comma_separated_tags = str(instance.tags).split(",")
    comma_separated_tags = [
        slugify(tag, allow_unicode=True) for tag in comma_separated_tags]

    for tag_name in comma_separated_tags:
        tag, is_success = Tag.objects.update_or_create(
            name=tag_name, defaults={'name': tag_name})
        HasTag.objects.create(post=instance, tag=tag)


sys.modules[__name__] = Tag
