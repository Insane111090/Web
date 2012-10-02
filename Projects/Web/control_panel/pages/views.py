# Create your views here.
from django.shortcuts import render
from datetime import datetime
import os
def home(request):
	context={'ts':datetime.now()}
	return render(request,'home.html',context)

def listing(request,direct):
	direct='/etc/'+direct
	context={'dir_content':os.listdir(direct)}
	return render(request,'listing.html',context)
