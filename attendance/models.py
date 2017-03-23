from django.db import models
from datetime import date
from django.contrib.auth.models import User

def upload_in_profiles(instance, filename):
	"""
	Returns path to profiles directory
	"""
	return 'profiles/user_{0}/{1}'.format(instance.user.id, filename)

def upload_in_attendance(instance, filename):
	"""
	Returns path to attendance directory corresponding
	to current date and user id
	"""
	today = date.now()
	today_path = today.strftime('%Y/%m/%d')

	return 'attendance/{2}/user_{0}/{1}'.format(instance.user.id, filename, today_path)

class Student(models.Model):
	"""
	class to store Student Profile

	Fields - 
		- user : Foreign key to User
		- rollno : unique roll number of a student
		- first_name : First Name of a student
		- last_name : Last Name of a student
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	rollno = models.IntegerField(unique=True, blank=False, null=False)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	id_img = models.ImageField(upload_to=upload_in_profiles)

class Attendance(models.Model):
	"""
	class to store student attendance on each date

	Fields - 
		- student : ForeignKey to Student class
		- attendance : True or False, whether present or not
		- class_date : Date Time the class is taken
	"""
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	attendance = models.BooleanField(default=False, null=False)
	class_date = models.DateTimeField(auto_now_add=True)
	id_img = models.ImageField(upload_to=upload_in_attendance)




