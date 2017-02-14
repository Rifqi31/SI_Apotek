from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.

class costumer(models.Model):

	kd_costumer = models.CharField(primary_key = True, default = '', max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')], unique = True)
	nama_costumer = models.CharField(max_length = 15)
	alamat_costumer = models.TextField()
 	


	def __unicode__(self):
		return self.kd_costumer