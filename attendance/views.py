from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import StudentForm, AttendanceForm

from google.cloud import vision

import io

from .vision_helpers import *

def get_vision_client():
	return vision.Client()

def class_mood(request):
	faces = []

	if request.method == 'POST':
		img, uri = '', ''

		if request.FILES:
			img = request.FILES['img']
		else:
			uri = request.POST['link']

		client = get_vision_client()

		if img:
			faces = detect_faces(img)
		else:
			faces = detect_faces_uri(uri)

	return render(request, 'mood.html', {'content' : faces})