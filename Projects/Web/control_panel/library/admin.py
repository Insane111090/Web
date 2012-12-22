# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic
from library.models import *

class ImageAdmin(admin.TabularInline):
        model=BooksImage
	extra=1

class AuthorAdmin(admin.ModelAdmin):
	list_display=('last_name','first_name','email',)
	list_display_links=('last_name','first_name',)
	ordering=('last_name','first_name')

class BookAdmin(admin.ModelAdmin):
	list_display=('title','publisher','publication_date',)
	list_display_links=('title',)
	search_fields=('title',)
	date_hierarchy='publication_date'
        fieldsets=(
                (None,{'fields':('title','authors')}),
                ('Выходные данные',{
                        'description':u'Издательство и дата выпуска',
                        'fields': ('publisher',),
                        })
                )
	inlines=[ImageAdmin,]


class PublisherAdmin(admin.ModelAdmin):
	list_display=('title','country','city',)
	list_display_links=('title',)
	list_filter=('country','city',)
	ordering=('title',)
	fieldsets=(
		(None,{'fields':('title',)}),
		('Контактная информация',{
			'description':u'Издательство и дата выпуска',
			'fields': ('country','city','address'),
			})
		)

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
#admin.site.register(BooksImage,ImageAdmin)
