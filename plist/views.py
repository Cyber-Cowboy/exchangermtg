import json
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CardList, Card
from .forms import CardForm

import json
import requests

def index(request):
	cardlist = CardList.objects.all()
	return render(request,
		"plist/index.html",{"cardlists":cardlist})

def card_search(request):
	cards = []
	query = request.GET.get("query", "")
	if query:
		cards = Card.objects.filter(Q(name__icontains=query))
	return render(request, "plist/search.html", {"cards":cards})

def card_list(request, pk):
	card_list = get_object_or_404(CardList,pk=pk)
	return render(request,
		"plist/cardlist.html", {"card_list":card_list})

@login_required(redirect_field_name='my_redirect_field')
def create_card_list(request):
	if request.method == "POST":
		cardlist = CardList(user=request.user, name=request.POST["name"])
		cardlist.save()
		return HttpResponseRedirect(reverse("plist:card_list", args=[cardlist.pk,]))
	else:
		return render(request, "plist/create_list.html", {})

def create_card(request):
	errors = []
	options = CardList.objects.filter(user=request.user)
	if request.method=="POST":
		form = CardForm(request.POST)
		response = requests.get("https://api.scryfall.com/cards/named?exact=%s"%request.POST["name"])
		if json.loads(response.content)["object"]=="error":
			errors.append("This card does not exist!")
			return render(request, "plist/create_card.html", {"options":options,
														"errors":errors})
		if form.is_valid:
			form.save()
			return HttpResponseRedirect("/")
	return render(request, "plist/create_card.html", {"options":options,
														"errors":errors})

@login_required(redirect_field_name='my_redirect_field')
def my_lists(request):
	lists = CardList.objects.filter(user=request.user)
	return render(request, "plist/my_lists.html", {"lists":lists})
