from django.urls import path
from .views import *

# router links
urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
    path('contact/', contact, name='contact'),
	path('<slug:slug>/', detail, name="detail"),
	path('tagged/<slug:slug>/', tagged, name="tagged"),
]