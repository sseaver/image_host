"""image_host URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app.views import (IndexView, UserCreateView, ProfileView, PostCreateView, PostDetailCommentCreateView,
                       PostUpdateView, PostDeleteView, CommentUpdateView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^accounts/profile/$', ProfileView.as_view(), name="profile_view"),
    url(r'^post/create/$', PostCreateView.as_view(), name="post_create_view"),
    url(r'^post/(?P<pk>\d+)/$', PostDetailCommentCreateView.as_view(), name="post_detail_comment_create_view"),
    url(r'^post/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name="post_update_view"),
    url(r'^post/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name="post_delete_view"),
    url(r'^comment/(?P<pk>\d+)/update/$', CommentUpdateView.as_view(), name="comment_update_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
