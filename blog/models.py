from django.db import models
from django.utils import timezone
from django.db.models import permalink


class Topic(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique=True)

	def __str__(self):
		return self.title


class Image(models.Model):
	image = models.ImageField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)


class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique=True, unique_for_date='publish')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	topic = models.ForeignKey(Topic, blank=True, null=True)
	image = models.ImageField(blank=True, null=True)
	truncate_words = models.IntegerField(default=50)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.title
