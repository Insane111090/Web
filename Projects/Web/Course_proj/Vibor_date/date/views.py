# Create your views here.
from django.shortcuts import render
from datetime import datetime
from date.models import Date
import os


def home(request):
	return render(request,'home.html')
def result(request):
	name = request.POST.get('user','')
	date = request.POST.get('entered_date','')
	newItem = Date(name = name, date = date)
	newItem.save()
	return render(request,'result.html')

