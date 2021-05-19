import sys

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.urls import reverse

from blogApp.models import Post
from authenticationApp.models import Profile
from blogApp.forms import PostForm


@login_required
def createBlogView(request):
    context = {}
    form = PostForm(request.POST or None,  request.FILES or None)

    user = request.user
    profile = Profile.get_profile_by_user(user)

    if not profile.is_verified:
        return redirect(reverse('authenticationApp:account-verification'))

    if request.method == "POST":

        if form.is_valid():
            instance = form.save(commit=False)

            instance.slug = slugify(instance.slug, allow_unicode=True)
            instance.author = request.user
            tags = instance.tags.split(',')
            tags = [slugify(tag, allow_unicode=True) for tag in tags]
            instance.tags = ",".join(tags)
            instance.save()

            form.save_m2m()

            messages.success(request, "Article created")

            return HttpResponseRedirect(reverse('blogApp:detail', args=(instance.slug,)))
        else:
            for error in form.errors:
                messages.error(request, error)

    context["form"] = form
    context["create"] = True

    return render(request, "blogApp/create_blog_form.html", context)


sys.modules[__name__] = createBlogView
