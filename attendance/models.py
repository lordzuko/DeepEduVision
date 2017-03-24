from django.db import models
from datetime import date
from django.contrib.auth.models import User

def upload_in_profiles(instance, filename):
	"""
	Returns path to profiles directory
	"""
	return 'profiles/user_{0}/{1}'.format(instance.user.id, filename)

class Faculty(models.Model):
	"""
	class to store Student Profile

	Fields - 
		- user : Foreign key to User
		- first_name : First Name of a student
		- last_name : Last Name of a student
		- profile_img : Profile Picture
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	profile_img = models.ImageField(upload_to=upload_in_profiles, null=True)
	about_me = models.CharField(max_length=150)
	contact = models.IntegerField(null=True)

	class Meta:
		db_table = 'faculty'
