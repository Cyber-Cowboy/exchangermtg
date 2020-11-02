import json
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CardList, Card
from .forms import CardForm

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

@login_required(redirect_field_name='my_redirect_field')
def create_card_list(request):
	if request.method == "POST":
		cardlist = CardList(user=request.user, name=request.POST["name"])
		cardlist.save()
		return HttpResponseRedirect(reverse("plist:card_list", args=[cardlist.pk,]))
	else:
		return render(request, "plist/create_list.html", {})

def create_card(request):
	if request.method=="POST":
		form = CardForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect("/")
	else:
		options = CardList.objects.filter(user=request.user)
	return render(request, "plist/create_card.html", {"options":options})

@login_required(redirect_field_name='my_redirect_field')
def my_lists(request):
	lists = CardList.objects.filter(user=request.user)
	return render(request, "plist/my_lists.html", {"lists":lists})