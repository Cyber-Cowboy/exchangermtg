import json
import requests
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class CardList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=15, blank=True)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("plist:card_list", args=[self.pk])

class Card(models.Model):
	name = models.CharField(max_length=100)
	mset = models.CharField(max_length=5)
	foil = models.BooleanField(default=False)
	alt_art = models.BooleanField(default=False)
	my_price = models.FloatField()
	card_list = models.ForeignKey(CardList, on_delete=models.CASCADE)
	condition = models.CharField(max_length=2, choices=[("M","M"),
												("NM","NM"),
												("SP","SP"),
												("HP","HP")], default="NM")

	def __str__(self):
		return self.name
	
	def get_market_price(self):
		response = requests.get("https://api.scryfall.com/cards/named?exact=%s"%self.name)
		return json.loads(response.content)["prices"]["usd"]
