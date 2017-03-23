from django import forms
from .models import Student, Attendance

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('user', 'rollno', 'first_name', 'last_name', 'id_img', )

class AttendanceForm(forms.ModelForm):
	class Meta:
		model = Attendance
		fields = ('student', 'attendance', 'id_img', )