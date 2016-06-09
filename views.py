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

def game1(request):
	if request.method == "POST"
		form = form(request.POST)
		my_number = form.cleaned_data.get("my_number")
		my_number.save()
		return render(request, "game2.html")

def game2(request):
	if request.method == "POST":
		form = Form(request.POST)
		guess_number = form.cleanead_data.get("guess_numbber")
		#otehr_number = player2.my_number
		ball = 0, strike =0
		a = guess_number // 1000; guess_number -= a * 1000;
		b = guess_number // 100; guess_number -= b * 100;
		c = guess_number // 10; guess_number -= c * 10;
		d = guess_number;
		guess_list = [a,b,c,d]
		"""
		e = other_number // 1000; other_number -= e * 1000;
		f = other_number // 100; other_number -= g * 100;
		g = other_number // 10; other_number -= h * 10;
		h = other_number;
		other_list = [e, f, g, h]
		for i in range(4):
			for j in range(4):
				if other_list[i] == guess_number[j]:
					ball++
		for in in range(4):
			if other_list[i] == guess_number[i]:
				ball--
				strike++
		states = str(strike) + "스트라이커" + str(ball) + "볼"
		states 디비에 저장

		if strike==4:
			return render(request, "win.html")
		else:
			return render(requst, "game2.html", {form을 리턴하면 방정보같은 쓸데없는게 나갈거같지만 일단 form을 리턴})
		"""

	return render(request,"game2.html")	


def waits(request):
	if request.method == "POST":
		for i in range(1000):
			nicnameList = player.objects.all()
			if len(nicnameList) < 2:
				form.save()
				return render(request,"game.html", {"form":form ,"nicnameList":nicnameList,})
			time.sleep(2)
	return render(request,"waits.html",{"form":form})