from game.models import *
from django import forms

class Form(forms.ModelForm):
	class Meta:
		model = player
		fields = ['nicname','room']
	
	def clean_nicname(self):
		nicname = self.cleaned_data.get('nicname')
		return nicname

	def clean_room(self):
		room = self.cleaned_data.get('room')
		return room


class Form_mynum(forms.ModelForm):
	class Meta:
		model = player_num 
		fields = ['mynumber','room']

	def clean_mynumber(self):
		mynumber = self.cleaned_data.get('mynumber')
		return mynumber


class Form_numberList_room1(forms.ModelForm):
	class Meta:
		model = number_room1
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number


class Form_numberList_room2(forms.ModelForm):
	class Meta:
		model = number_room2
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number


class Form_numberList_room3(forms.ModelForm):
	class Meta:
		model = number_room3
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number


class Form_numberList_room4(forms.ModelForm):
	class Meta:
		model = number_room4
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number


class Form_numberList_room5(forms.ModelForm):
	class Meta:
		model = number_room5
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number


class Form_numberList_room6(forms.ModelForm):
	class Meta:
		model = number_room6
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number


class Form_numberList_room7(forms.ModelForm):
	class Meta:
		model = number_room7
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number


class Form_numberList_room8(forms.ModelForm):
	class Meta:
		model = number_room8
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number


class Form_numberList_room9(forms.ModelForm):
	class Meta:
		model = number_room9
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number


class Form_numberList_room10(forms.ModelForm):
	class Meta:
		model = number_room10
		fields = ['guess_number','number_judgment']
	
	def clean_guess_number(self):
		guess_number = self.cleaned_data.get('guess_number')
		return guess_number