import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Card

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
def change_my_price(request):
	card_id = json.loads(request.body)["card_id"]
	my_price = json.loads(request.body)["my_price"]
	card = get_object_or_404(Card, pk=card_id)
	if card.card_list.user == request.user:
		card.my_price = my_price
		card.save()
		return JsonResponse({"success":True})
	else:
		return JsonResponse({"success":False})