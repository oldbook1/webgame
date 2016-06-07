from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.shortcuts import render_to_response, RequestContext
from models import *
from django.forms import *
from .forms import Form
import time


def startpage(request):
	if request.method == "POST":
		form = Form(request.POST)
		nicnameList = player.objects.all()
		if len(nicnameList) < 2 :
			if form.is_valid():
				form.save()
				for i in range(1000):
					nicnameList = player.objects.all()
					if len(nicnameList) >= 2:
						return render(request,"game.html", {"form":form ,"nicnameList":nicnameList,})
					time.sleep(2)
		if len(nicnameList) >= 2 :
			return render(request,"waits.html",{"form":form})

	form = Form()

	return render(request,"home.html",{ "form":form, })

def game(request):
	return render(request,"game.html")	


def waits(request):
	if request.method == "POST":
		for i in range(1000):
			nicnameList = player.objects.all()
			if len(nicnameList) < 2:
				form.save()
				return render(request,"game.html", {"form":form ,"nicnameList":nicnameList,})
			time.sleep(2)
	return render(request,"waits.html",{"form":form})