from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "plist"
urlpatterns = [
	path("exchanger/<int:pk>/cards", views.get_cards),
	path("exchanger/<int:pk>", views.card_list, name="card_list"),
	path("exchanger/create", views.create_card_list, name="create_card_list"),
	path("exchanger/create_card", views.create_card, name="create_card"),
	path("exchanger/my", views.my_lists, name="my_lists"),
	path("", views.index, name="index")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)