from django.contrib import admin
from django.db import models
from .models import Post, Topic, Image

from pagedown.widgets import AdminPagedownWidget


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    exclude = ['publish']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['-created', 'status']

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

class TopicAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Image)

