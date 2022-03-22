from matplotlib.style import context
from users.models import Appointment2
from .models import Product
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from users.forms import AppointmentForm

# Create your views here.

def home (request):

	products = Product.objects.filter(status = 1)

	context = {
		'products': products
	}

	return render(request, 'web/it_home.html', context)


@login_required
def appointment (request):
	#messages.info(request, f'You have to be logged in to make appointments')
	if request.method == 'POST':

		first_name = request.POST.get('firstname')
		last_name= request.POST.get('lastname')
		phone= request.POST.get('phone')
		email=request.POST.get('email')
		subject= request.POST.get('subject')
		description = request.POST.get('description')
		appointmentForm = Appointment2(first_name= first_name, last_name= last_name, phone = phone, email= email,
										 subject = subject, description= description)
		
		appointmentForm.save()
		messages.success(request, f'{first_name},  You have succesfully booked an appointment, you will receive further instructions on the email provided')
		return redirect ('appointment')

	else: 

		appointmentForm = Appointment2()


	return render (request, 'web/make_appointment.html')


def shop_detail2 (request, slug):

	#related = Product.objects.filter(slug != slug )
	if (Product.objects.filter(slug = slug, status = 1)):
		products = Product.objects.filter(slug = slug)



		context = {
			'products': products
		}

		return render(request, 'web/shop_detail2.html', context)	
 
	else:
		
		messages.warning(request, "no such products on our platform")
		return redirect ('shop_detail2')



	


def test (request):
	return render(request, 'web/test.html')

def about (request):
	return render(request, 'web/it_about.html')	


def services (request):
	return render(request, 'web/services.html')


def price (request):
	return render(request, 'web/price.html')

def contact (request):
	return render(request, 'web/contact.html')


def contact2 (request):
	return render(request, 'web/contact2.html')	


def privacy_policy (request):
	return render(request, 'web/privacy_policy.html')

def faq (request):
	messages.success(request, f'welcome to the FAQ page')
	return render(request, 'web/faq.html')

def shop (request):
	products = Product.objects.filter(status = 1)

	context = {
		'products': products
	}

	return render(request, 'web/shop.html', context)


def shop_detail (request):
	return render(request, 'web/shop_detail.html')



def error (request):
	return render(request, 'web/error.html')	


def career (request):
	return render(request, 'web/career.html')		


def cart (request):
	return render(request, 'web/cart.html')	


#def checkout (request):
#	return render(request, 'web/checkout.html')	

def services_detail (request):
	return render(request, 'web/services_detail.html')


def services_list (request):
	return render(request, 'web/services_list.html')



def blog_detail (request):
	return render(request, 'web/blog_detail.html')


def blog_list (request):
	return render(request, 'web/blog_list.html')


def blog_grid (request):
	return render(request, 'web/blog_grid.html')




