import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from blogApp.models import Post

from blogApp.models import Tag


def tagView(request, tagname):
    context = {}
    tag = get_object_or_404(Tag, name=tagname)

    context["tag_name"] = tagname
    context["articles"] = Post.get_posts_by_tag_name(tag.name)

    return render(request, 'blogApp/tag.html', context)


sys.modules[__name__] = tagView
