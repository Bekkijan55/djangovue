from django.db import models

# Create your models here.

class Task(models.Model):
	TODO = 0
	DONE = 1

	STATUS_CHOICES = (
		(TODO, 'To Do'),
		(DONE, 'Done')
		)
	description = models.CharField(max_length=255)
	status = models.IntegerField(choices=STATUS_CHOICES, default=TODO)

class User(models.Model):
	url = models.CharField(max_length=200)
	username = models.CharField(max_length=250)
	email = models.CharField(max_length=250)

class Group(models.Model):
	url = models.CharField(max_length=250)
	name = models.CharField(max_length=250)	

	