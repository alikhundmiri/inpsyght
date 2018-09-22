from django.shortcuts import render
from django.http import (
	Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse


from .forms import InterestedForm


def index(request):
	context = {
		'show_last_div' : False,
	}

	# return render(request, 'base.html', context)
	return HttpResponseRedirect(reverse('landing_patients'))
	# This line above will redirect to landing_patients page.

def landing_patients(request):
	if request.method == "POST":
		form = InterestedForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(reverse('thankyou_page'))
	else:
		form = InterestedForm()

	context = {
		'form' : form,
		'show_last_div' : False,
	}
	return render(request, 'core/landing_patients.html', context)


def landing_agents(request):
	if request.method == "POST":
		form = InterestedForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(reverse('thankyou_page'))
	else:
		form = InterestedForm()

	context = {
		'show_last_div' : False,
	}
	return render(request, 'core/landing_agents.html', context)

def thankyou_page(request):
	context = {
		'show_last_div' : False,
	}
	return render(request, 'core/thankyou_page.html', context)
	
