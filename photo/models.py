from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
	owner = models.ForeignKey(User)
	url = models.CharField(max_length=200)
	pubDate = models.DateTimeField('data da publicacao')
	
class Vote(models.Model):
	user = models.ForeignKey(User)
	photo = models.ForeignKey(Photo)
	vote = models.IntegerField()
