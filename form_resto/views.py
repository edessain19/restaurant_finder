from django.shortcuts import render
from .forms import RequestForm
from .models import Request
from .get_request import *

# Create your views here.

class Result:
	def __init__(self, name, adress, rating, image, price, link):
		self.name = name
		self.adress = adress
		self.rating = rating
		self.image = image
		self.price = price
		self.link = link

def request_create_view(request):
	check_result = 0
	result_of_request = []
	adress, dist, price, lang, food = "", 0, 0, "", ""
	
	form = RequestForm()
	if request.method == 'POST':
		form = RequestForm(request.POST)
		if form.is_valid():
			adress, dist, price, lang, food = parsing_value(form)
			print(adress, dist, lang)
		data = request_api(adress, dist, price, lang, food, 10)
		if data == "error":
			check_result = -1
		else :
			check_result = 1
		result_of_request = parse_api(data)
		if len(result_of_request) < 10 and check_result == 1:
			data_2 = request_api(adress, dist * 2, price, lang, 'all', 10 - len(result_of_request))
			result_of_request_2 = parse_api(data_2)
			result_of_request = result_of_request + result_of_request_2
	context = {
		'form' : form,
		'result' : result_of_request,
		'check_result' : check_result
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
	if (resto == -1):
		return ("error")
	lst = []
	for elem in resto:
		name, address, rating, image, price, link = "", "", 0, "", 0, ""
		for key, value in elem.items():
			if key == 'name':
				name = value
			if key == 'location':
				address = value['address1'] + ' - ' + value['zip_code'] + ' ' + value['city'] + ', ' + value['country']
			if key == 'rating':
				rating = value
			if key == 'image_url':
				image = value
			if key == 'price':
				price = value
			if key == 'url':
				link = value
		tmp = Result(name, address, rating, image, price, link)
		lst.append(tmp)
	return (lst)

