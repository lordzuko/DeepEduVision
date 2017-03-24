from django.db import models
from datetime import date
from django.contrib.auth.models import User

def upload_in_profiles(instance, filename):
	"""
	Returns path to profiles directory
	"""
	return 'media/profiles/{0}/{1}'.format(instance.user.id, filename)

class Faculty(models.Model):
	"""
	class to store Faculty Profile

	Fields - 
		- user : Foreign key to User
		- first_name : First Name of a student
		- last_name : Last Name of a student
		- profile_img : Profile Picture
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30, null=True, blank=True)
	last_name = models.CharField(max_length=30, null=True, blank=True)
	profile_img = models.ImageField(upload_to=upload_in_profiles, null=True, blank=True)
	about_me = models.CharField(max_length=150, null=True, blank=True)
	contact = models.IntegerField(null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'faculty'
