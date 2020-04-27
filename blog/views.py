from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from . import mixins
from .models import Post, Topic


class PostListView(mixins.PageTitleMixin, ListView):
	"""Displays a list of Posts (Archive Page)"""
	model = Post
	page_title = "Web Development and Design Blog | sunnyville"
	pageinate_by = 10

	# def get_queryset(self, *args, **kwargs):
	#     return Post.objects.filter(status = 'published')


class TopicPostListView(mixins.PageTitleMixin, ListView):
	"""Displays a list of Posts in a Topic"""
	model = Post
	template_name = "blog/topic_post_list.html"

	def get_page_title(self):
		topic = get_object_or_404(Topic, slug=self.kwargs['slug'])
		return "{} | sunnyville".format(topic.title)

	def get_queryset(self, *args, **kwargs):
	    return Post.objects.filter(topic__slug = self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(TopicPostListView, self).get_context_data(**kwargs)

		topic = get_object_or_404(Topic, slug=self.kwargs['slug'])

		context['topic_title'] = topic.title
		context['count'] = self.get_queryset().count()

		return context


class PostDetailView(DetailView):
	"""Displays Post Detail (Single Post)"""
	model = Post
