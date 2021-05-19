import sys

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, reverse

from blogApp.models import Post


@login_required
def deleteBlogView(request, slug):
    article = Post.objects.get(slug=slug)

    if article.author != request.user:
        return HttpResponseForbidden()

    article.delete()

    messages.success(request, "Successfully deleted")

    return HttpResponseRedirect(reverse('blogApp:home'))


sys.modules[__name__] = deleteBlogView
