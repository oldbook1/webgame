from django.db import models


class player(models.Model):
	nicname = models.CharField(max_length=50, null=False)

	def __unicode__(self):
		return self.nicname