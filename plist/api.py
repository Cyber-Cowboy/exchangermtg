import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Card, CardList
from .forms import CardForm

def get_cards(request, pk):
	card_list = get_object_or_404(CardList, pk=pk)
	cards = [{
		"name":card.name,
		"my_price":card.my_price,
		"condition":card.condition,
		"display":True,
		"foil":card.foil,
		"price":-1,
		"id":card.id} for card in Card.objects.filter(card_list=card_list)]

	return JsonResponse(cards, safe=False)

def get_market_price(request):
	card_id = json.loads(request.body)["id"]
	card = get_object_or_404(Card, pk=card_id)
	return JsonResponse({"price":card.get_market_price()})

@login_required
def delete_card(request):
	card_id = json.loads(request.body)["card_id"]
	card = get_object_or_404(Card, pk=card_id)
	if card.card_list.user == request.user:
		card.delete()
		return JsonResponse({"success":True})
	else:
		return JsonResponse({"success":False})

@login_required
def change_card(request):
	card_id = json.loads(request.body)["id"]
	my_price = json.loads(request.body)["my_price"]
	condition = json.loads(request.body)["condition"]
	card = get_object_or_404(Card, pk=card_id)
	if card.card_list.user == request.user:
		card.my_price = my_price
		card.condition = condition
		card.save()
		return JsonResponse({"success":True})
	else:
		return JsonResponse({"success":False})

@login_required
def add_new_card(request):
	card_data = json.loads(request.body)
	print(card_data)
	card_list = get_object_or_404(CardList, pk=int(card_data['card_list']))
	form = CardForm({"name":card_data["name"],
					"my_price":card_data["my_price"],
					"condition":card_data["condition"]})

	if form.is_valid() and request.user==card_list.user:
		form.clean()
		cd = form.cleaned_data
		card = Card(name=cd["name"],
					my_price=cd["my_price"],
					condition=cd["condition"],
					card_list=card_list,
					foil=False,
					alt_art=False,
					mset="IXL")
		card.save()
		return JsonResponse({"success":True})
	else:
		return JsonResponse({"success":False})
