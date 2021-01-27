from django.urls import path
from . import views, api

app_name = "plist"
urlpatterns = [
	path("exchanger/<int:pk>/cards", views.get_cards),
	path("exchanger/<int:pk>", views.card_list, name="card_list"),
	path("exchanger/create", views.create_card_list, name="create_card_list"),
	path("exchanger/create_card", views.create_card, name="create_card"),
	path("exchanger/my", views.my_lists, name="my_lists"),
	path("edit_cardlist/", views.create_card, name="edit_cardlist"),
	path("delete_card/", api.delete_card, name="delete_card"),
	path("change_my_price/", api.change_my_price, name="change_my_price"),
	path("add_new_card/", api.add_new_card, name="add_new_card"),
	path("", views.index, name="index")
] 