import sys

from django.shortcuts import render
from django.contrib import messages

from blogApp.models import Post
from authenticationApp.models import Profile


def searchView(request):
    context = {}
    keyword = request.GET.get("keyword")
    search_type = request.GET.get("searchtype")
    has_query_params = (keyword != None) and (type != None)

    if has_query_params:
        context["result_type"] = search_type

        if search_type == "Article" and keyword != "":
            context["results"] = Post.objects.filter(
                title__icontains=keyword, public=True)
        elif search_type == "Author" and keyword != "":
            context["results"] = Profile.objects.filter(
                user__username__icontains=keyword)
        else:
            context["results"] = []

        return render(request, 'blogApp/searchresult.html', context)

    return render(request, 'blogApp/search.html', context)


sys.modules[__name__] = searchView
