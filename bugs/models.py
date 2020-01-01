from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


CHOICES = (
	(0, 'Received'),
	(1, 'In progress'),
	(2, 'Done')
)

class Bug(models.Model):

	"""
	Creates a bug post model on the database
	"""

	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bugs_posts')
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=CHOICES, default=0)
	views = models.IntegerField(default=0)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
	



