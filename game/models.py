from django.db import models


class player(models.Model):
	nicname = models.CharField(max_length=50, null=False)
	room = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.nicname
	
	def __unicode__(self):
		return self.room