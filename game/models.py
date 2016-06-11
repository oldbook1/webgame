from django.db import models


class player(models.Model):
	nicname = models.CharField(max_length=50, null=False, unique = True)
	room = models.IntegerField(default = 0 , null=False)
	cnt = models.IntegerField(default = 1 , null=False, unique = True)

	def __unicode__(self):
		return self.nicname
	
	def __unicode__(self):
		return self.room
	
	def __unicode__(self):
		return self.cnt


class player_num(models.Model):
	mynumber = models.IntegerField(null = False , default = 123, unique = True)
	room = models.IntegerField(default = 0 , null=False)
	cnt = models.IntegerField(default = 1 , null=False, unique = True)

	def __unicode__(self):
		return self.mynumber

	def __unicode__(self):
		return self.room
	
	def __unicode__(self):
		return self.cnt



class number_room(models.Model):
	guess_number = models.IntegerField(null = False , default = 123, unique = True)
	ball  = models.IntegerField(null = False )
	strike  = models.IntegerField(null = False )

	def __unicode__(self):
		return self.guess_number

	def __unicode__(self):
		return self.ball

	def __unicode__(self):
		return self.strike

