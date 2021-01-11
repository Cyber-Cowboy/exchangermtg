from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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