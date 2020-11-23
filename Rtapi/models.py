from django.db import models

# Create your models here.

class Project(models.Model):
	projectname=models.CharField(max_length=200,blank=False, default='')
	description=models.CharField(max_length=200,blank=False, default='')
	targeturl=models.CharField(max_length=200,blank=False, default='')
	logfile=models.FileField(upload_to='')
	connectiontimout=models.CharField(max_length=200,blank=False, default='')
	sendtimeout=models.CharField(max_length=200,blank=False, default='')
	receivetimeout=models.CharField(max_length=200,blank=False, default='')
	


class Scan(models.Model):
	projectname=models.CharField(max_length=200,blank=False, default='')
	testmode=models.CharField(max_length=200,blank=False, default='')
	scandatetime=models.CharField(max_length=200,blank=False, default='')
		