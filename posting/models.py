from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=50)
	date = models.DateField()
	author = models.CharField(max_length=10)
	post = models.TextField()

	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ["-id"]