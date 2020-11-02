from django.forms import ModelForm
from .models import Card

class CardForm(ModelForm):
	class Meta:
		model = Card
		fields = ["name", "foil", "alt_art", "card_list"]