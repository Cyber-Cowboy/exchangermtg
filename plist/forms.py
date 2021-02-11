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
	set = forms.CharField(max_length=20)

	def clean(self):
		cleaned_data = super().clean()
		raw_name = self.cleaned_data.get("name")
		raw_set = self.cleaned_data.get("set")
		raw_response = requests.get("https://api.scryfall.com/cards/named?exact="+raw_name+"&set="+raw_set)
		response = json.loads(raw_response.content)
		if not "name" in response.keys():
			self.add_error("name", "not found in the set")
		else:
			self.cleaned_data["name"] = response["name"]
