from django import template
from blog.models import Post, Topic

register = template.Library()

@register.inclusion_tag('blog/main_nav.html')
def main_nav_items():
	''' Displays Top Bar, with Logo and Navigation '''
	topics = Topic.objects.filter(post__isnull=False).distinct()
	return {'topics':topics}

@register.inclusion_tag('blog/tags/post_archive.html', takes_context=True)
def post_archive(context):
    ''' Shows List of Items on Archive Pages '''
    return {
        'post_list': context['post_list'],
        'paginator': context['paginator'],
        'is_paginated': context['is_paginated'],
        'MEDIA_URL': context['MEDIA_URL'],
    }
