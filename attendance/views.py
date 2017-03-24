from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from google.cloud import vision
from PIL import Image, ImageFont, ImageDraw
import urllib.request
import io, random, copy

from .vision_helpers import *

def get_vertices(faces):
	vertices = []
	for face in faces:
		vertices.append(face.fd_bounds.vertices)

	return vertices

def build_faces_border(vertex,dr):
	x1 = vertex[0].x_coordinate
	y1 = vertex[0].y_coordinate
	x2 = vertex[1].x_coordinate
	y2 = vertex[1].y_coordinate

	dr.rectangle([(x1,y1),(x2,y2)],outline='yellow')


def build_faces_border_all(vertices, path):
	im = Image.open("media/{}".format(path))
	dr = ImageDraw.Draw(im)

	for vertex in vertices:
		vertex = (vertex[0],vertex[2])
		build_faces_border(vertex, dr)

	im.save("media/mod{0}".format(path))

def save_uploaded_file(img):
	rndm = random.random()
	with open('media/temp{}.png'.format(rndm), 'wb+') as dest:
		for chunk in img.chunks():
			dest.write(chunk)

	return 'temp{}.png'.format(rndm)

def class_mood(request):
	template_name = 'mood.html'
	context = {}
	faces = []

	if request.method == 'POST':
		img, uri = '', ''

		if request.FILES:
			img = request.FILES['img']
			clone_img = copy.deepcopy(img)
			filename = save_uploaded_file(clone_img)
		else:
			uri = request.POST['link']
			rndm = random.random()
			filename = "temp{}.png".format(rndm)
			urllib.request.urlretrieve(uri, filename)


		client = vision.Client()

		if img:
			faces = detect_faces(img)
		else:
			faces = detect_faces_uri(uri)

		vertices = get_vertices(faces)

		build_faces_border_all(vertices, filename)

		context = {
			'faces' : faces,
			'head_count' : len(faces),
		}

	return render(request, template_name, context)