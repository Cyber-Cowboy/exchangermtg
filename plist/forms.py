import json
import requests
from django import forms
from django.core.exceptions import ValidationError

class CardForm(forms.Form):
	name = forms.CharField(max_length=100)
	condition = forms.ChoiceField(choices=[("M","M"),
											("NM","NM"),
											("SP","SP"),
											("HP","HP")])
	my_price = forms.FloatField()

	def clean_name(self):
		raw_name = self.cleaned_data["name"]
		raw_response = requests.get("https://api.scryfall.com/cards/named?exact="+raw_name)
		response = json.loads(raw_response.content)
		if "name" in response.keys():
			return response["name"]
		else:
			raise ValidationError("Name not found")
