from django.contrib.auth.models import User 
from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from .models import Billinginfo



class UserRegisterForm(UserCreationForm):

	 email = forms.EmailField()
	 first_name = forms.CharField()
	 last_name = forms.CharField()
	 Address = forms.CharField(required =False)

	 

	 class Meta:
	 	model = User
	 	fields = ['first_name','last_name','username','Address','email','password1','password2']
	

		
class BillingForm(forms.ModelForm):

	class Meta:
		model = Billinginfo
		fields = ['first_name','last_name','company_name','country','city', 'postcode', 'phone','address','email']
	 	



