from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
import datetime
import os
# Create your models here.

def get_file_path (request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename  = "%s%s" % (nowTime, original_filename)

    return os.path.join('pictures/', filename)
def texting():
	text = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo."
	return text

def texting2():
	text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ac elementum elit. Morbi eu arcu ipsum. Aliquam lobortis accumsan quam ac convallis. Fusce elit mauris, aliquet at odio vel, convallis vehicula nisi. Morbi vitae porttitor dolor. Integer eget metus sem. Nam venenatis mauris vel leo pulvinar, id rutrum dui varius. Nunc ac varius quam, non convallis magna. Donec suscipit commodo dapibus. \n \n Vestibulum et ullamcorper ligula. Morbi bibendum tempor rutrum. Pelle tesque auctor purus id molestie ornare.Donec eu lobortis risus. Pellentesque sed aliquam lorem. Praesent pulvinar lorem vel mauris ultrices posuere. Phasellus elit ex, gravida a semper ut, venenatis vitae diam. Nullam eget leo massa. Aenean eu consequat arcu, vitae scelerisque quam. Suspendisse risus turpis, pharetra a finibus vitae, lobortis et mi."	
	return text

class Comment (models.Model):
	
	user = models.ForeignKey(User, on_delete = models.CASCADE )
	Email = models.EmailField()
	Phone = models.IntegerField()
	Password = models.CharField(max_length = 20)
	Comment = models.TextField()
	
	date = models.DateTimeField(default = timezone.now)


	def __str__(self):
		return f'{self.user.username} Comment'

class Product (models.Model):
	slug = models.SlugField(max_length= 50, null= False, blank=False)
	img = models.ImageField(upload_to = get_file_path, null= True, blank =True)
	product_name = models.CharField(max_length=50, null= False, blank=False)
	old_price = models.FloatField( null= False, blank=False)
	new_price = models.FloatField( null= False, blank=False)
	ratings = models.IntegerField()
	status = models.BooleanField(default= True, help_text= "0 = not available, 1= available")
	quantity = models.IntegerField(null= False, blank=False)

	small_description = models.TextField(max_length= 500, null= False, blank=False, default= texting)
	big_description = models.TextField(max_length=3000, null= False, blank=False, default= texting2)
	meta_title = models.CharField(max_length= 150, null= False, blank= False)
	meta_keywords = models.CharField(max_length= 150, null= False, blank= False)
	meta_description = models.TextField(max_length= 500, null= False, blank= False)
	created_at = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.product_name

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	product_qty = models.IntegerField(null = False, blank = False)
	created_at = models.DateTimeField(auto_now_add= True)

	
