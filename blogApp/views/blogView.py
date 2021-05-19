import sys

from django.shortcuts import render
from django.contrib import messages

from blogApp.models import Post
from authenticationApp.models import Profile


def blogView(request, username=None):
    context = {}
    context["blog_name"] = username
    has_params = (username != None)

    if has_params:
        profile = Profile.get_profile_by_username(username)

        if request.user.username == username:
            context["articles"] = profile.get_articles(include_private=True)
        else:
            context["articles"] = profile.get_articles()

    return render(request, 'blogApp/blog.html', context)


sys.modules[__name__] = blogView
