from django.contrib import admin

# Register your models here.
from history.models import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'contentType', 'viewed_on', 'content_object')
    search_fields = ['user', 'contentType', 'content_object']


admin.site.register(History, HistoryAdmin)
