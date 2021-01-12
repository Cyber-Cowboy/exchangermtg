from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
app_name = "exchprofile"
urlpatterns = [
	path('login/', LoginView.as_view(template_name="exchprofile/login.html"), name="login" ),
	path('logout/', LogoutView.as_view(), name="logout" ),
	path('registration/', views.registration, name="registration"),
	path("profile/<str:username>/", views.user_profile, name="user_profile"),
] 