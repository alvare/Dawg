from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=30)
	mail = models.EmailField(blank=True)
	content = models.TextField()
	verse = models.ImageField(upload_to='verses', blank=True)
	coda = models.ImageField(upload_to='codas', blank=True)
	time = models.DateTimeField(auto_now=True)
	online = models.BooleanField()
	def __unicode__(self):
		return self.title
