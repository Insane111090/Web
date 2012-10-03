# Create your views here.
from django.shortcuts import render
from datetime import datetime
import os
def home(request):
	context={'ts':datetime.now()}
	return render(request,'home.html',context)

def listing(request,direct):
	dir=[]
	fl=[]
	direct='/home/'+direct
	for dN,d,f in os.walk(direct):
		if dN == direct:
			os.chdir(direct)
			for i in f:
				fl.append({"name":i,"size":os.path.getsize(i),"modified":datetime.fromtimestamp(int(os.path.getmtime(i))),})
			dir = d
	context={'dir_content':dir,'file_content':fl}
	return render(request,'listing.html',context)
