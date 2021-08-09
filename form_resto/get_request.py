
import requests
import json
from mysite.settings import API_KEY

def request_api(adress, dist, price, lang, food, limit):
	ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
	HEADERS = {'Authorization': 'bearer %s' % API_KEY}
	PARAMETERS = {'term': 'restaurants',
				'limit': limit,
				'price' : price,
				'radius': dist * 1000,
				'location': adress,
				'categories': food,
				'locale' : lang,
				}
	response = requests.get(url = ENDPOINT,
							params = PARAMETERS,
							headers = HEADERS)
	data = response.json()
	return data

def parsing_value(form):
	adress, dist, price, lang, food = "", 0, 0, "", {"italian" : 0, "lebanese" : 0, "japanese" : 0, "belgian" : 0}
	for key, value in form.cleaned_data.items():
		if key == 'localisation':
			adress = value
		if key == "distance":
			dist = value
			if dist > 45:
				dist = 45
			if dist < 1:
				dist = 1
		if key == "price":
			price = value
		if key == "language_of_query":
			lang = value + "_BE"
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
	return (adress, dist, price, lang, type_of_food[1:])






# https://github.com/areed1192/sigma_coding_youtube/blob/master/python/python-api/yelp-api/Yelp%20API%20-%20Business%20Search.py
# https://www.youtube.com/watch?v=GJf7ccRIK4U&t=138s
# https://www.youtube.com/watch?v=uz5gyXemak0&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=25


# 	Introduction
# At LIZY we love food, and we enjoy trying new places for lunch! Please help us by developing an application that suggests good restaurants to order from.
# General:
# * backend:
#     * Rest API
#     * Authenticated (choose whichever methods seems safest to you)
#     * Validate inputs as much as possible
# * frontend:
#     * UI to communicate with the API (query and display the result)
# * Language / framework / no framework, up to you
# * Integrate with third party providers to search for restaurant information: Yelp ? Google ? Or another external provider
# * Hosting environment is up to you, we just need a public address to test the application
# * Some tests (integration / unit) with some mocks to test out parts of developed features
# Inputs:
# * Localisation
# * Max distance from localisation
# * Price range in euros
# * Attendees - Take into account the attendees’ cuisine type preferences
#     * Gilles likes: [ Italian, Lebanese, Japanese, Belgian]
#     * Vince likes: [ Italian, Japanese, Lebanese ]
#     * Sam likes: [ Belgian ]
#     * Klaas likes: [ Japanese, Belgian ]
#     * Gaelle likes: [ Japanese, Lebanese ]
# Outputs:
# * List of 10 best restaurants / places to lunch given the inputs
# * Try to make it that the best matching restaurants come first, but you still allow suggestions for restaurants that match less
# Deliverables:
# * access to git repo
# * suggest the deadline



# recuperer l'info dans class
# utiliser les classes pour recuperer les infos du formulaire
#  no-sql django?