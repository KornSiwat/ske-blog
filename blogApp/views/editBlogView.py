import sys

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from django.urls import reverse

from blogApp.models import Post
from blogApp.forms import PostForm


@login_required
def editBlogView(request, slug):
    context = {}
    article = get_object_or_404(Post, slug=slug)

    if article.author != request.user:
        return HttpResponseForbidden()

    form = PostForm(request.POST or None, instance=article)

    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.slug = slugify(instance.title)
            instance.author = request.user
            instance.save()

            form.save_m2m()

            messages.success(request, "Successfully edit")
            return HttpResponseRedirect(reverse('blogApp:detail', args=(instance.slug,)))

            
    context["form"] = form
    context["create"] = False

    return render(request, "blogApp/create_blog_form.html", context)


sys.modules[__name__] = editBlogView
