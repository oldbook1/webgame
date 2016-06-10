from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render_to_response, RequestContext
from models import *
from django.forms import *
from .forms import *
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
				if room < 11 : # room>0
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
	nicnameListAll = player.objects.all()
	my_numberListAll = player_num.objects.all()
	nicnameList = {}
	nicnameList = dict()
	for nic in nicnameListAll:
		if nic.room == room :
			nicnameList += nic
	my_numberList = {}
	my_numberList = dict()
	for number in my_numberListAll:
		if number.room == room :
			my_numberList += number
	
	if len(my_numberList) < 2:
		if request.method == "POST":
			form_num = Form_mynum(request.POST)
			if form_num.is_valid():
				mynumber = form_num.cleaned_data['mynumber']
				if mynumber > 123 :# && my_number < 987
					if mynumber/100 != mynumber/10: # && (100,10), &&(100,1),&& (10,1)
						form_num = Form_mynum(
							{'mynumber' : mynumber,'room' : room,}
						)
						form_num.save()
						return render(request, "game2.html", {"nicnameList":nicnameList,"form_num":form_num,} )
				form_num = Form_mynum()
				return render(request,"game.html", {"nicnameList":nicnameList,"my_numberList":my_numberList,})

	if len(my_numberList) == 2:
		if request.method == "POST":
			form_guess = Form_numberList_room1(request.POST)
			guess_number = form_guess.cleanead_data.get("guess_number")
			#otehr_number = player2.my_number
			#ball = 0, strike =0
			a = guess_number // 100; guess_number -= b * 100;
			b = guess_number // 10; guess_number -= c * 10;
			c = guess_number;
			guess_list = [a,b,c]
			"""
			e = other_number // 100; other_number -= g * 100;
			f = other_number // 10; other_number -= h * 10;
			g = other_number;
			other_list = [e, f, g]
			for i in range(3):
				for j in range(3):
					if other_list[i] == guess_number[j]:
						ball++
			for in in range(3):
				if other_list[i] == guess_number[i]:
					ball--
					strike++
			number_judgment = str(strike) + "strike " + str(ball) + "ball"
			form_guess = Form_numberList_room1(
					{'my_number' : my_number,'room' : room,}
			)
			form_guess.save()

			if strike==3:
				return render(request, "win.html")
			else:
				return render(requst, "game2.html", {"form":form})
			"""
		form_guess = Form_numberList_room1()
		return render(request,"game2.html", {"nicnameList":nicnameList,"form_guess":form_guess,})
	form_num = Form_mynum()
	return render(request,"game.html", {"nicnameList":nicnameList,"form_num":form_num,})