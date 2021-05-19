import sys

from django.shortcuts import render
from django.contrib import messages

from blogApp.models import Post
from blogApp.models import Banner
from blogApp.models import ContentSection

from blogApp.models import Tag


def homeView(request):
        
    context = {}

    context['banners'] = Banner.get_banners()
    context['tags'] = Tag.get_tags()
    context['content_sections'] = ContentSection.get_content_sections()
    context['articles'] = Post.get_posts()
    context['first_articles'] = Post.get_posts().first()
    context['last_articles'] = Post.get_posts().last()

    return render(request, "blogApp/home.html", context)


sys.modules[__name__] = homeView
