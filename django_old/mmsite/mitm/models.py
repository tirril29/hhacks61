from django.db import models

# Create your models here.
# Users
class User(models.Model):
	#information for the system. 
	username = models.CharField(max_length = 100)
	#Record Keeping
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 256)
	email = models.CharField(max_length = 256)


class Dispute(models.Model):
	u1 = models.ForeignKey(User)
	description = models.CharField(max_length = 1024)
'''
	u2 = models.ForeignKey(user)
	m = models.ForeignKey(user)
'''