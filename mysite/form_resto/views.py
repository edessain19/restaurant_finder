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