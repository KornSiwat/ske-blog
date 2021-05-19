from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blogApp.views import createBlogView
from blogApp.views import deleteBlogView
from blogApp.views import detailBlogView
from blogApp.views import editBlogView
from blogApp.views import homeView
from blogApp.views import tagView
from blogApp.views import searchView
from blogApp.views import blogView
from blogApp.views import likeView


app_name = 'blogApp'

urlpatterns = [
    path('', homeView, name='home'),
    path('create/', createBlogView, name='create'),
    path('tag/<str:tagname>/', tagView, name="tag"),
    path('delete/<str:slug>/', deleteBlogView, name='delete'),
    path('detail/<str:slug>/', detailBlogView.as_view(), name='detail'),
    path('edit/<str:slug>/', editBlogView, name='edit'),
    path('blog/<slug:username>', blogView, name='blog'),
    path('search/', searchView, name='search'),
    path('like/', likeView, name='post_like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
