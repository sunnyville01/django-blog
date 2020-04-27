from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^topic/(?P<slug>[\w-]+)/$', views.TopicPostListView.as_view(), name='topic-post-list'),
    url(r'^(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^$', views.PostListView.as_view(), name='list'),
]
