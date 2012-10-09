# Create your views here.
from django.shortcuts import render
from datetime import datetime
from library.models import Book, Author
import os

def home(request):
	context={'ts':datetime.now()}
	return render(request,'home.html',context)

def listing(request,direct):
	dr=[]
	fl=[]
	direct='/home/'+direct
	for dN,d,f in os.walk(direct):
		if dN == direct:
			os.chdir(direct)
			for i in f:
				fl.append({"name":i,"size":os.path.getsize(i),"modified":datetime.fromtimestamp(int(os.path.getmtime(i))),})
			dr = d
	context={'dir_content':dr,'file_content':fl}
	return render(request,'listing.html',context)

def books_list(request,dr):
	list=Book.objects.all()
	context={'book':list}
	return render(request,'bookslist.html',context)

def book_info(request,dr):
	book=Book.objects.get(id__exact=dr[:-1])
	context={'bookinf':book,
		'book_auth':book.authors.all()}
	return render(request,'bookinfo.html',context)	


def author(request,dr):
	context={'author':Author.objects.get(id__exact=dr[:-1])}
	return render(request,'author.html',context)

def authors_list(request):
	context={'author':Author.objects.all()}
	return render(request,'authors_list.html',context)
