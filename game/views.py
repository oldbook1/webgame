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
					{'nicname' : nicname,'room' : i,'cnt': cnt,},
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
				if 0< room < 11 :
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


def game(request, room00, cnt00):
	nicnameList = player.objects.filter(room = int(room00))
	for nic in nicnameList:
		if nic.cnt != int(cnt00):
			other_cnt = nic.cnt
	
	my_numberList = player_num.objects.filter(room = int(room00))
	guessList1 = number_room.objects.filter(cnt = int(cnt00))
	guessList2 = number_room.objects.filter(cnt = int(other_cnt))

	m = int(room00)
	k = int(cnt00)
	

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
									{'mynumber' : mynumber,'room' : room00,'cnt': cnt00},
								)	
								form_num.save()
								form_guess = Form_numberList()
								for i in range(1000):
									my_numberListAll = player_num.objects.filter(room = int(room00))	
									if len(my_numberListAll) == 2:
										if k < other_cnt:
											return render(request, "game2.html", {"nicnameList":nicnameList,"form_guess":form_guess,}) 
										if k > other_cnt:
											return redirect('/game2/%d/%d/'%(int(room00), int(cnt00)))
									time.sleep(2)

		form_num = Form_mynum()
		return render(request,"game.html", {"nicnameList":nicnameList,"form_num":form_num})

	#guess_number input
	if len(my_numberList) == 2:
		if request.method == "POST":
			form_guess = Form_numberList(request.POST)
			if form_guess.is_valid():
				guess_number = form_guess.cleaned_data['guess_number']
				if 122 < guess_number< 988:
					if guess_number/100 != (guess_number-(guess_number/100)*100)/10:
						if guess_number/100 != guess_number-((guess_number/10)*10):
							if (guess_number-(guess_number/100)*100)/10 != guess_number-((guess_number/10)*10):
								for my_num in my_numberList:
									if my_num.cnt != int(cnt00):
										other_number = my_num.mynumber

								ball = 0
								strike = 0
								a = guess_number / 100 
								guess_number -= a * 100
								b = guess_number / 10 
								guess_number -= b * 10
								c = guess_number
								guess_list = [a,b,c]
	
								e = other_number / 100
								other_number -= e * 100
								f = other_number / 10 
								other_number -= f * 10
								g = other_number
								other_list = [e, f, g]

								for i in range(3):
									for j in range(3):
										if other_list[i] == guess_list[j]:
											ball += 1
								for i in range(3):
									if other_list[i] == guess_list[i]:
										ball-= 1
										strike+= 1

								guess_number = form_guess.cleaned_data['guess_number']
								form_guess = Form_numberList(
										{'guess_number' : guess_number,'ball' : ball, 'strike':strike,'room':m,'cnt':k},
								)
								form_guess.save()

								if strike==3:
									context = 'you win'
									return render(request, "end.html", {'context':context} )
								if strike <3:
									return redirect('/game2/%d/%d/'%(int(room00), int(cnt00)))
		
		form_guess = Form_numberList()
		return render(request,"game2.html", {"nicnameList":nicnameList,"guessList1":guessList1,'guessList2':guessList2,"form_guess":form_guess,})
	form_guess = Form_numberList()
	return render(request,"game2.html", {"nicnameList":nicnameList,"guessList1":guessList1,'guessList2':guessList2,"form_guess":form_guess,})


def game2(request, room00, cnt00):
	nicnameList = player.objects.filter(room = int(room00))
	my_numberList = player_num.objects.filter(room = int(room00))
	for nic in nicnameList:
		if nic.cnt != int(cnt00):
			other_cnt = nic.cnt
	guessList1 = number_room.objects.filter(cnt = int(cnt00))
	guessList2 = number_room.objects.filter(cnt = int(other_cnt))

	if request.method == "POST":
		for i in range(1000):
			roomList = number_room.objects.filter(room = int(room00))
			count_turn = len(roomList)
			if int(cnt00) > other_cnt:
				if count_turn%2 == 1:
					for room_end in roomList:
						if room_end.strike == 3:
							nicnameList.delete()
							my_numberList.delete()
							roomList.delete()
							context = 'you lose'
							return render(request, "end.html", {'context':context})
					return redirect('/game/%d/%d/'%(int(room00), int(cnt00)))
			if int(cnt00) < other_cnt:
				if count_turn%2 == 0:
					for room_end in roomList:
						if room_end.strike == 3:
							nicnameList.delete()
							my_numberList.delete()
							roomList.delete()
							context = 'you lose'
							return render(request, "end.html", {'context':context})
					return redirect('/game/%d/%d/'%(int(room00), int(cnt00)))
			for room_end in roomList:
				if room_end.strike == 3:
					nicnameList.delete()
					my_numberList.delete()
					roomList.delete()
					context = 'you lose'
					return render(request, "end.html", {'context':context} )
			time.sleep(2)
			

	return render(request,"game3.html",{"nicnameList":nicnameList,"guessList1":guessList1,'guessList2':guessList2,})