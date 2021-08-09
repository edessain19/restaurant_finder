from django.shortcuts import render
from .forms import RequestForm
from .models import Request
from .get_request import *

# Create your views here.

def request_create_view(request):
	check_result = 0
	result_of_request = []
	adress, dist, price, food = "", 0, 0, ""
	
	form = RequestForm()
	if request.method == 'POST':
		form = RequestForm(request.POST)
		if form.is_valid():
			adress, dist, price, food = parsing_value(form)
		data = request_api(adress, dist, price, food, 10)
		if data == "error":
			check_result = -1
		else :
			check_result = 1
		result_of_request = parse_api(data)
		if len(result_of_request) < 10 and check_result == 1:
			data_2 = request_api(adress, dist * 2, price, 'all', 10 - len(result_of_request))
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
		name, address, rating, image, price = "", "", 0, "", 0
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
		tmp = Result(name, address, rating, image, price)
		lst.append(tmp)
	return (lst)

def parsing_value(form):
	adress, dist, price, food = "", 0, 0, {"italian" : 0, "lebanese" : 0, "japanese" : 0, "belgian" : 0}
	for key, value in form.cleaned_data.items():
		if key == 'localisation':
			adress = value
		if key == "max_dist":
			dist = value
		if key == "price":
			price = value
		if key == "Gilles":
			if value == True:
				food["italian"] += 1 
				food["lebanese"] += 1
				food["japanese"] += 1
				food["belgian"] += 1
		if key == "Vince":
			if value == True:
				food["italian"] += 1
				food["lebanese"] += 1
				food["japanese"] += 1
		if key == "Sam":
			if value == True:
				food["belgian"] += 1
		if key == "Klaas":
			if value == True:
				food["japanese"] += 1
				food["belgian"] += 1
		if key == "Gaelle":
			if value == True:
				food["lebanese"] += 1
				food["japanese"] += 1
	type_of_food = ""
	max_value = max(food.values())
	for k,v in food.items(): 
		if v == max_value:
			type_of_food = type_of_food + "," + k
	return (adress, dist, price, type_of_food[1:])