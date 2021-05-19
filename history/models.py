from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

from .signals import object_viewed_signal


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contentType = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True)  # collect blog comment
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('contentType')
    viewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content_object} view {self.viewed_on}"

    class Meta:
        verbose_name_plural = "Histories"


def object_viewed_reciever(sender, instance, request, *args, **kwargs):
    new_history = History.objects.create(
        user=request.user,
        contentType=ContentType.objects.get_for_model(sender),
        object_id=instance.id,
    )


object_viewed_signal.connect(object_viewed_reciever)
