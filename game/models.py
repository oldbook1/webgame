from django.db import models


class player(models.Model):
	nicname = models.CharField(max_length=50, null=False, unique = True)
	room = models.IntegerField(default = 0 , null=False)

	def __unicode__(self):
		return self.nicname
	
	def __unicode__(self):
		return self.room


class player_num(models.Model):
	my_number = models.IntegerField(null = False , default = 1234, unique = True)
	room = models.IntegerField(default = 0 , null=False)

	def __unicode__(self):
		return self.my_number


class number_room1(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number


class number_room2(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number


class number_room3(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number


class number_room4(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number


class number_room5(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number


class number_room6(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number


class number_room7(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number


class number_room8(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number


class number_room9(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number


class number_room10(models.Model):
	guess_number = models.IntegerField(null = False , default = 1234, unique = True)
	number_judgment  = models.CharField(max_length=5,null = False )

	def __unicode__(self):
		return self.guess_number