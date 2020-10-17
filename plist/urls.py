from django.urls import path
from . import views

urlpatterns = [
	path("exchanger/<int:pk>/cards", views.get_cards),
	path("exchanger/<int:pk>", views.card_list),
]