from django.contrib import admin

from blogApp.models import Post
from blogApp.models import Comment
from blogApp.models import Banner
from blogApp.models import ContentSection
from blogApp.models import HasContent
from blogApp.models import Tag
from blogApp.models import HasTag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'public', 'created_on')
    list_filter = ("public",)
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ['body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Banner)
admin.site.register(ContentSection)
admin.site.register(HasContent)
admin.site.register(Tag)
admin.site.register(HasTag)
