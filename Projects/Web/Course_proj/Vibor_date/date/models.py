# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.

class Date(models.Model):
	name=models.CharField('Имя пользователя',max_length=6)
	date=models.DateTimeField('Введенная дата',auto_now=True)
	def __unicode__(self):
		return u'%s %s' % (self.name, self.date)
	
