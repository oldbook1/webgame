from game.models import *
from django import forms

class Form(forms.ModelForm):
	class Meta:
		model = player
		fields = ['nicname']
	
	def clean_nicname(self):
		nicname = self.cleaned_data.get('nicname')
		return nicname