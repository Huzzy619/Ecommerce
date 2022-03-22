from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from matplotlib.pyplot import cla
from pytz import timezone
from django.utils import timezone




# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')


	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self , *args , **kwargs):
		super().save(*args , **kwargs)

	# This resizes the pictures uploaded
		img = Image.open(self.image.path) 
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Billinginfo(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	address = models.CharField (max_length = 500)
	email = models.EmailField()
	country = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	postcode = models.IntegerField()
	phone = models.CharField(max_length= 13)
	first_name = models.CharField (max_length = 50)
	last_name = models.CharField (max_length = 50) 
	company_name = models.CharField(max_length = 100)
	
	


	def __str__(self):
		return f'{self.user.username} Billing information'



class Appointment2 (models.Model):
	# user = models.ForeignKey(User, on_delete = models.CASCADE)
	first_name = models.CharField (max_length = 50)
	last_name = models.CharField (max_length = 50) 
	email = models.EmailField()
	phone = models.CharField(max_length= 13)
	subject = models.CharField(max_length= 100)
	description = models.TextField()
	time = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return f'{self.user.username} appointment details'

	
