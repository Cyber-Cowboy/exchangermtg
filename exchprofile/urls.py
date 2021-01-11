from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import registration
app_name = "exchprofile"
urlpatterns = [
	path('login/', LoginView.as_view(template_name="exchprofile/login.html"), name="login" ),
	path('logout/', LogoutView.as_view(), name="logout" ),
	path('registration/', registration, name="registration"),
] 