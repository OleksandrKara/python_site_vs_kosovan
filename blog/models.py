from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField('Name', max_length=50)
    slug = models.SlugField('Slug')

class Meta:
	verbose_name = 'Category'
	verbose_name_plural = 'Categories'

	def __unicode__(self):
		return u'%s' % self.name


class EntryManager(models.Manager):
    def published(self):
        return self.filter(draft=False)
    def drafted(self):
        return self.filter(draft=True)


class BlogEntry(models.Model):
    title = models.CharField('Title', max_length=50)
    slug = models.SlugField('Slug')
    tease = models.TextField('Tease (summary)', blank=True)
    body = models.TextField('Content')
    draft = models.BooleanField('Is draft', default=True)
    created_at = models.DateTimeField('Date of creation', default=datetime.now)
    published_at = models.DateTimeField('Date of publication', default=datetime.now)
	category = models.ForeignKey(Category, related_name='entries')

	objects = EntryManager()

class Meta:
	verbose_name = 'Blog entry'
	verbose_name_plural = 'Blog entries'
	ordering = ('-published_at',)

	def __unicode__(self):
		return u'%s' % self.title

from django.contrib import admin
admin.site.register(BlogEntry)
admin.site.register(Category)