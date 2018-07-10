from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Feeds(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=False )
	status = models.CharField(max_length=150)
	date_created = datetime.now()
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.last_modified


class Articles(models.Model):
	title = models.CharField(max_length=100)
	article = models.TextField()
	author= models.ForeignKey(User, on_delete=models.CASCADE, null=False)
	date_created = datetime.now()
	last_modified = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title

class Messages(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=False )
	message = models.TextField()
	date_created = datetime.now()
	last_modified = models.DateTimeField(auto_now=True)



	def __str__(self):
		return self.message

# Create your models here.
