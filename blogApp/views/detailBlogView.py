import sys

# from django.views import View
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


from blogApp.models import Post, Comment
from blogApp.forms import PostForm, CommentForm
from history.mixins import ObjectViewMixin


class detailBlogView(ObjectViewMixin, View):

    def get_object(self, queryset=None):
        return Post.objects.get(slug=self.kwargs['slug'])

    def get(self, request, *args, **kwargs):
        context = {}
        post = get_object_or_404(Post, slug=kwargs['slug'])

        authorProfile = Post.get_author_profile_by_author(post.author)

        try:
            comments = Comment.objects.filter(
                post=post).order_by('-created_on')
        except:
            comments = []
        comment_form = CommentForm()

        context['is_liked'] = post.is_liked(request.user)
        context['post'] = post
        context['total_like'] = post.get_like_count()
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['authorProfile'] = authorProfile

        return render(request, 'blogApp/detail.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse('authenticationApp:login')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = self.get_object()
            new_comment.save()

        return HttpResponseRedirect(reverse_lazy('blogApp:detail', args=[self.kwargs['slug']]))

sys.modules[__name__] = detailBlogView
