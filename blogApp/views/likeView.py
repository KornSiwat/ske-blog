import sys

from blogApp.models import Post
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

@login_required
def likeView(request):
    # if request.method == 'POST' and request.is_ajax():
    if request.POST.get('action') == 'post': 
        flag = None
        postid = int(request.POST.get('post_id'))
        post = Post.get_post_by_id(postid)

        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
            post.save()
            flag = False
        else:
            post.like.add(request.user)
            post.save()
            flag = True
        
        return JsonResponse({'total_like': post.get_like_count(), 'flag': flag,})
    return HttpResponse("Error access denied")

sys.modules[__name__] = likeView