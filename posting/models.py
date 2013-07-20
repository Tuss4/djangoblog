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

class Comment(models.Model):
	author = models.CharField(max_length=30)
	date = models.DateField()
	email = models.EmailField()
	comment = models.TextField()
	actual_post = models.ForeignKey(Post)

	def __unicode__(self):
		return u'%s: %s by %s' % (self.actual_post, self.comment, self.author)

	class Meta:
		ordering = ["-id"]