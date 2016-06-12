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
			#random matching
			if room == 0:
				nicnameList = player.objects.all() 
				room_cheker = 0
				cnt = len(nicnameList) + 1 
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
					{'nicname' : nicname,'room' : room,'cnt': cnt,},
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
									return redirect('/game/%d/%d/'%(i, cnt))
					room_cheker = 0
					time.sleep(2)
			#room matching
			if room != 0:
				if room < 11 : # room>0
					nicnameList = player.objects.all() 
					room_cheker = 0
					cnt = len(nicnameList) + 1 
					form = Form(
						{'nicname' : nicname,'room' : room,'cnt': cnt,},
					)
					form.save()
					for i in range(1000): 
						nicnameList = player.objects.all()
						for nic in nicnameList:
							if nic.room == room:
								room_cheker += 1
						if room_cheker == 2:
							for i in range(1,10):
								if room == i:
									return redirect('/game/%d/%d/'%(i, cnt))	
						if room_cheker >2:
							break
						room_cheker = 0
						time.sleep(2)
        
	form = Form()
	return render(request,"home.html",{ "form":form, })


def game(request, room, cnt):
	nicnameListAll = player.objects.all()
	nicnameList = {}
	nicnameList = dict()
	for nic in nicnameListAll:
		if nic.room == room:
			nicnameList += nic
	for nic in nicnameList:
		if nic.cnt != cnt:
			other_cnt = nic.cnt
	
	my_numberListAll = player_num.objects.all()
	my_numberList = {}
	my_numberList = dict()
	for number in my_numberListAll:
		if number.room == room:
			my_numberList += number
	guessList1 = {}
	guessList2 = {}
	guessList1 = dict()
	guessList2 = dict()
	i = 0
	for numberList in my_numberList:
		if i%2 == 0:
			guessList1 += numberList
		if i%2 == 1:
			guessList2 += numberList
		i += 1
	j = room
	k = cnt
	

	#mynumber input
	if len(my_numberList) < 2:
		if request.method == "POST":
			form_num = Form_mynum(request.POST)
			if form_num.is_valid():
				mynumber = form_num.cleaned_data['mynumber']
				if 122 < mynumber< 988:
					if mynumber/100 != (mynumber-(mynumber/100)*100)/10:
						if mynumber/100 != mynumber-((mynumber/10)*10):
							if (mynumber-(mynumber/100)*100)/10 != mynumber-((mynumber/10)*10):
								form_num = Form_mynum(
									{'mynumber' : mynumber,'room' : j,'cnt': k}
								)	
								form_num.save()
								'''
								oomList = number_room.objects.all()		
								count_turn = len(roomList)
								'''
								form_guess = Form_numberList_room()
								for i in range(1000):
									my_numberListAll = player_num.objects.all()	
									my_numberList = {}
									num_cheker = 0
									for number in my_numberListAll:
										if number[2] == j :
											my_numberList += number
									if num_cheker == 2:
										if k < other_cnt:
											return render(request, "game2.html", {"nicnameList":nicnameList,"form_guess":form_guess,}) 
										if k > other_cnt:
											return redirect('/game2/%d/%d/'%(room, cnt))
									time.sleep(2)

		form_num = Form_mynum()
		return render(request,"game.html", {"nicnameList":nicnameList,"form_num":form_num})

	#guess_number input
	if len(my_numberList) == 2:
		'''
		for nic in nicnameList:
			if nic.cnt != cnt:
				other_cnt = nic.cnt
		for i in range(1000):
			roomList = number_room.objects.all()
			count_turn = len(roomList)
			if count_turn%2 == 0:
				if cnt < other_cnt:
					break
			if count_turn%2 == 1:
				if cnt > other_cnt:
					break
		for room_end in roomList:
			if room_end.strike == 3:
				context = 'you lose'
				return render(request, "end.html", {'context':context} )
		'''
		if request.method == "POST":
			form_guess = Form_numberList_room(request.POST)
			if form_guess.is_vaild():
				guess_number = form_guess.cleanead_data['guess_number']
				for my_num in my_numberList:
					if my_num.cnt != cnt:
						other_number = my_num.mynumber

				ball = 0
				strike = 0
				a = guess_number / 100 
				guess_number -= a * 100
				b = guess_number / 10 
				guess_number -= b * 10
				c = guess_number
				guess_list = {a,b,c}
	
				e = other_number / 100
				other_number -= e * 100
				f = other_number / 10 
				other_number -= f * 10
				g = other_number
				other_list = {e, f, g}

				for i in range(3):
					for j in range(3):
						if other_list[i] == guess_list[j]:
							ball += 1
				for i in range(3):
					if other_list[i] == guess_list[i]:
						ball-= 1
						strike+= 1

				guess_number = form_guess.cleanead_data['guess_number']
				form_guess = Form_numberList_room(
						{'guess_number' : guess_number,'ball' : ball, 'strike':strike},
				)
				form_guess.save()

				if strike==3:
					context = 'you win'
					return render(request, "end.html", {'context':context} )
				if strike <3:
					return redirect('/game2/%d/%d/'%(room, cnt))
	
		form_guess = Form_numberList_room()
		return render(request,"game2.html", {"nicnameList":nicnameList,"guessList1":guessList1,'guessList2':guessList2,"form_guess":form_guess,})
	form_guess = Form_numberList_room()
	return render(request,"game2.html", {"nicnameList":nicnameList,"guessList1":guessList1,'guessList2':guessList2,"form_guess":form_guess,})


def game2(request, room, cnt):
	nicnameListAll = player.objects.all()
	my_numberListAll = player_num.objects.all()
	nicnameList = {}
	nicnameList = dict()
	for nic in nicnameListAll:
		if nic.room == room:
			nicnameList += nic
	for nic in nicnameList:
			if nic.cnt != cnt:
				other_cnt = nic.cnt
	my_numberList = {}
	my_numberList = dict()
	for number in my_numberListAll:
		if number.room == room:
			my_numberList += number
	guessList1 = {}
	guessList2 = {}
	i = 0
	for numberList in my_numberList:
		if i%2 == 0:
			guessList1 += numberList
		if i%2 == 1:
			guessList2 += numberList

	if request.method == "POST":
		for i in range(1000):
			roomList = number_room.objects.all()
			count_turn = len(roomList)
			if count_turn%2 == 0:
				if cnt < other_cnt:
					for room_end in roomList:
						if room_end.strike == 3:
							context = 'you lose'
							return render(request, "end.html", {'context':context})
					return redirect('/game/%d/%d/'%(room, cnt))
			if count_turn%2 == 1:
				if cnt > other_cnt:
					for room_end in roomList:
						if room_end.strike == 3:
							context = 'you lose'
							return render(request, "end.html", {'context':context})
					return redirect('/game/%d/%d/'%(room, cnt))
			for room_end in roomList:
				if room_end.strike == 3:
					context = 'you lose'
					return render(request, "end.html", {'context':context} )
			time.sleep(2)
			

	return render(request,"game3.html",{"nicnameList":nicnameList,"guessList1":guessList1,'guessList2':guessList2,})