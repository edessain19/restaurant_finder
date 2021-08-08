from django import forms
from django.forms import ModelForm
from .models import Request


# ATTENDEES_CHOICES =(
#     ("1", "Gilles"),
#     ("2", "Vince"),
#     ("3", "Sam"),
#     ("4", "Klaas"),
#     ("5", "Gaelle"),
# )

class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = ['localisation', 
				'max_dist', 
				'price', 
				'Gilles',
				'Vince',
				'Sam',
				'Klaas',
				'Gaelle',
			]

# class RequestForm(forms.Form):
# 	localisation = forms.CharField(max_length=200)
# 	max_dist = forms.IntegerField()
# 	price_range = forms.IntegerField()
# 	attendees = forms.MultipleChoiceField(choices = ATTENDEES_CHOICES)