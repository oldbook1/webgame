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
		if form.is_valid():
			room = form.cleaned_data.get("room")
			if room == 0:    
				nicnameList = player.objects.all() 
				room_cheker = 0             
				for i in range(1,100):     
					for nic in nicnameList :
						if nic.room == i:   
							room_cheker += 1 
						if room_cheker ==2:  
							room_cheker = 0  
							break            
					if room_cheker != 0:    
						room_cheker = 0   
						form['room'] = i      
						break             
				form.save()
				for i in range(1000):  
					nicnameList = player.objects.all()
					for nic in nicnameList :
						if nic.room == room :
							room_cheker += 1
						if room_cheker == 2:
							return render(request,"game.html", {"form":form ,"nicnameList":nicnameList,})
					room_cheker = 0
					time.sleep(2)
			if room != 0:
				room_cheker = 0
				form.save()
				for i in range(1000): 
					nicnameList = player.objects.all()
					for nic in nicnameList :
						if nic.room == room :
							room_cheker += 1
						if room_cheker == 2:
							return render(request,"game.html", {"form":form ,"nicnameList":nicnameList,})
					room_cheker = 0
					time.sleep(2)
        
	form = Form()
	return render(request,"home.html",{ "form":form, })

def game(request):
	return render(request,"game.html")	
