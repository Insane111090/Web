# Create your views here.
from django.shortcuts import render
from datetime import datetime
from date.models import Date
from django.template import Context, Template
import os


def home(request):
	return render(request,'home.html')
def result(request):
	name = request.POST.get('user','')
	date = request.POST.get('entered_date','')
	newItem = Date(name = name, date = date)
	newItem.save()
	context = {'info':Date.objects.latest('id'),'cnt':Date.objects.count()}
	return render(request,'result.html',context)

