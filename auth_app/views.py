from django.shortcuts import render
from .forms import RegistrationForm, LoginForm

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from attendance.models import Faculty

def join(request):
	template_name = 'join.html'
	context = {'form' : RegistrationForm()}

	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			user = User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
			   	email=form.cleaned_data['email']
			)

			faculty = Faculty(
				user = user
			)

			faculty.save()

		return HttpResponseRedirect('/auth/login/')

    # GET Request
	return render(request, template_name, context)