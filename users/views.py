from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserRegisterForm,BillingForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import LoginView

# Create your views here.
 

def register (request):
	if request.method == "POST":

		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			
			messages.success(request, f'Account Created for {username} please login to continue')
			return redirect('login')

	else:	


		form = UserRegisterForm()

	return render (request, 'users/register.html', {'form': form})

@login_required
def profile (request):
	return render(request, 'users/profile.html')

def example (request):
	return render (request,'users/example.html' )

@login_required
def Billing (request):

	if request.method == 'POST':
		B_form = BillingForm(request.POST, instance = request.user.billinginfo)
		if B_form.is_valid():
			B_form.save()
			messages.success(request, f'Billing Information Saved successfully ')
			return redirect('home')

			
	else:

		B_form = BillingForm()

		
	return render (request  , 'users/billing.html', {'B_form' : B_form })




		

def login2 (request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username , password=password)
		if user is not None:
			login(request, user)

			messages.success(request, f'user logged in succesfully')
			return redirect('home')
		else:	
			messages.warning(request, f'invalid credentials')
			return redirect('login2')			
		
		



	return render (request, 'users/login2.html')

def logoutpage(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, f'you have logged out succesfully')
		return redirect('login')
