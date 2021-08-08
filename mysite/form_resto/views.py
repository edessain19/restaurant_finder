from django.shortcuts import render
from .forms import RequestForm
from .models import Request
from .get_request import *

# Create your views here.

def request_create_view(request):
	form = RequestForm()
	adress, dist = "", 0
	if request.method == 'POST':
		form = RequestForm(request.POST)
		if form.is_valid():
			for key, value in form.cleaned_data.items():
				if key == 'localisation':
					adress = value
				if key == "max_dist":
					dist = value
	data = request_api(adress, dist)
	result_of_request = parse_api(data)
	context = {
		'form' : form,
		'result' : result_of_request,
	}
	return render(request, "resto/form.html", context)

def check_businesses(data):
	if 'businesses' in data:
		for key, value in data.items():
			if key == 'businesses':
				return (value)
	else:
		return (-1)

def parse_api(data):
	resto = check_businesses(data)
	lst = []
	if (resto == -1):
		return ("error")
	for elem in resto:
		name, adress, rating, image, price = "", "", 0, "", 0
		for key, value in elem.items():
			if key == 'name':
				name = value
			if key == 'display_adress':
				adress = value
			if key == 'rating':
				rating = value
			if key == 'image_url':
				image = value
			if key == 'price':
				price = len(value)
		tmp = Result(name, adress, rating, image, price)
		lst.append(tmp)
	return (lst)