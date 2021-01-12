from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def registration(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('plist:index')
	else:
		form = UserCreationForm()
	return render(request,"exchprofile/registration.html", {"form":form})
def user_profile(request, username):
	return render(request, "exchprofile/profile.html", {"user":get_object_or_404(User, username=username)})