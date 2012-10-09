# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.

class Author(models.Model):
	first_name=models.CharField('Имя', max_length=32)
	last_name=models.CharField('Фамилия', max_length=32)
	email=models.EmailField('Электронная почта', null=True, blank=True)
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
	list_display=('get_author')
	title=models.CharField('Название',max_length=32)
	authors=models.ManyToManyField('Author')
	publisher=models.ForeignKey('Publisher', verbose_name='Publisher')
	publication_date=models.DateTimeField('Дата выпуска',auto_now=True)
	def __unicode__(self):
		return u'%s' % (self.title)
	def get_author(self):
		return ', '.join([str(a) for a in self.authors.all()])
	def get_absolute_url(self):
		return '/library/books/%i' % self.id

class Publisher(models.Model):
	title=models.CharField('Название',max_length=32)
	address=models.TextField('Адрес')
	city=models.CharField('Город',max_length=64)
	country=models.CharField('Страна',max_length=64)
	website=models.URLField('Адрес сайта')
	def __unicode__(self):
		return u'%s (%s)' % (self.title,self.website) 
