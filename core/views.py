from django.shortcuts import render
from django.http import (
	Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse
# Create your views here.


def index(request):
	context = {
		'show_last_div' : False,
	}

	# return render(request, 'base.html', context)
	return HttpResponseRedirect(reverse('landing_patients'))
	# This line above will redirect to landing_patients page.

def landing_patients(request):
	context = {
		'show_last_div' : False,
	}
	return render(request, 'core/landing_patients.html', context)


def landing_agents(request):
	context = {
		'show_last_div' : False,
	}
	return render(request, 'core/landing_agents.html', context)
