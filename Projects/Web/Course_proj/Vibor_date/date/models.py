# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.

class Date(models.Model):
	name=models.CharField('Имя пользователя',max_length=6)
	date=models.DateTimeField('Введенная дата',auto_now=True)
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
	def get_absolute_url(self):
		return '/date/Date/%i' % self.id
