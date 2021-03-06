from django.urls import path
from . import views, api

app_name = "plist"
urlpatterns = [
	path("exchangers/search", views.card_search, name="card_search"),
	path("exchanger/<int:pk>", views.card_list, name="card_list"),
	path("exchanger/create", views.create_card_list, name="create_card_list"),
	path("exchanger/create_card", views.create_card, name="create_card"),
	path("exchanger/my", views.my_lists, name="my_lists"),
	path("get_cards/<int:pk>", api.get_cards, name="get_cards"),
	path("edit_cardlist/", views.create_card, name="edit_cardlist"),
	path("delete_card/", api.delete_card, name="delete_card"),
	path("change_card/", api.change_card, name="change_card"),
	path("add_new_card/", api.add_new_card, name="add_new_card"),
	path("get_market_price/", api.get_market_price, name="get_market_price"),
	path("", views.index, name="index")
]
