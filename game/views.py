from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render_to_response, RequestContext
from models import *
from django.forms import *
from .forms import Form
import time


def startpage(request):
	if request.method == "POST":  
		form = Form(request.POST)
		if form.is_valid():
			nicname = form.cleaned_data['nicname']
			room = form.cleaned_data['room']
			if room == 0:
				nicnameList = player.objects.all() 
				room_cheker = 0             
				for i in range(1,10):
					for nic in nicnameList :
						if nic.room == i:   
							room_cheker += 1 
						if room_cheker ==2:
							if i == 10:
								form = Form()
								return render(request,"home.html",{ "form":form, })
							break            
					if room_cheker < 2 :    
						room_cheker = 0   
						room = i     
						break
					room_cheker = 0
				form = Form(
					{'nicname' : nicname,'room' : room,},
				)
				form.save()
				for i in range(1000):  
					nicnameList = player.objects.all()
					for nic in nicnameList :
						if nic.room == room :
							room_cheker += 1
						if room_cheker == 2:
							for i in range(1,10):
								if room == i:
									return redirect('/game/%d/' %i)
					room_cheker = 0
					time.sleep(2)
			if room != 0:
				if room < 11:
					room_cheker = 0
					form.save()
					for i in range(1000): 
						nicnameList = player.objects.all()
						for nic in nicnameList :
							if nic.room == room :
								room_cheker += 1
						if room_cheker == 2:
							for i in range(1,10):
								if room == i:
									return redirect('/game/%d/' %i)	
						if room_cheker >2:
							break
						room_cheker = 0
						time.sleep(2)
        
	form = Form()
	return render(request,"home.html",{ "form":form, })


def game(request, room):
	nicnameList = player.objects.all()
	if request.method == "POST":
		form = form(request.POST)
		my_number = form.cleaned_data.get("my_number")
		my_number.save()
		return render(request, "game2.html")

	return render(request,"game.html",{"nicnameList":nicnameList,})	


def game2(request):
	if request.method == "POST":
		form = Form(request.POST)
		guess_number = form.cleanead_data.get("guess_numbber")
		#otehr_number = player2.my_number
		#ball = 0, strike =0
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
		states = str(strike) + "strike " + str(ball) + "ball"
		states.save()

		if strike==4:
			return render(request, "win.html")
		else:
			return render(requst, "game2.html", {"form":form})
		"""

	return render(request,"game2.html")
