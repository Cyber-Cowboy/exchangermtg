import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import CardList, Card

def card_list(request, pk):
	return render(request, 
		"plist/cardlist.html", {})	
def get_cards(request, pk):
	card_list = CardList.objects.get(pk=pk)
	cards = [{
	"name":card.name,
	"my_price":card.my_price,
	"condition":card.condition,
	"display":True,
	"foil":card.foil,
	"price":card.get_market_price()}
	for card in Card.objects.filter(card_list=card_list)]
	return HttpResponse(json.dumps(cards))