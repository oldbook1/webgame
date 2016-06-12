from django.db import models


class player(models.Model):
	nicname = models.CharField(max_length=50, null=False, unique = True)
	room = models.IntegerField(default = 0 , null=False)
	cnt = models.IntegerField(default = 1 , null=False)

	def __unicode__(self):
		return unicode(self.nicname)
	
	def __unicode__(self):
		return unicode(self.room)
	
	def __unicode__(self):
		return unicode(self.cnt)


class player_num(models.Model):
	mynumber = models.IntegerField(null = False , default = 123, unique = True)
	room = models.IntegerField(default = 0 , null=False)
	cnt = models.IntegerField(default = 1 , null=False)

	def __unicode__(self):
		return unicode(self.mynumber)

	def __unicode__(self):
		return unicode(self.room)
	
	def __unicode__(self):
		return unicode(self.cnt)



class number_room(models.Model):
	guess_number = models.IntegerField(null = False , default = 123, unique = True)
	ball  = models.IntegerField(default =0 )
	strike  = models.IntegerField(default =0)
	room = models.IntegerField(default =0 )
	cnt = models.IntegerField(default =0)

	def __unicode__(self):
		return unicode(self.guess_number)

	def __unicode__(self):
		return unicode(self.ball)

	def __unicode__(self):
		return unicode(self.strike)

	def __unicode__(self):
		return unicode(self.room)
	
	def __unicode__(self):
		return unicode(self.cnt)

