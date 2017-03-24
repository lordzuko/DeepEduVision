from django.conf.urls import url
from django.contrib.auth import views as auth_views
from auth_app import views, forms

urlpatterns = [
	url(r'^join/', views.join, name='join'),

 	url(r'^login/', auth_views.login, {'template_name' : 'login.html', 'authentication_form' : forms.LoginForm}, name='login'),
 	url(r'^logout/', auth_views.logout, {'next_page' : '/login/'}, name='logout'),

 	#url(r'^forgot_password/', views.forgot, name='forgot'),
]
