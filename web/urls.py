from .import views as myviews 
from django.urls import path,include
from .cart import addtocart



urlpatterns = [
   
    path('', myviews.home, name = 'home'),
    path('make_appointment/', myviews.appointment, name= 'appointment'),
    path('about/', myviews.about, name= 'about'),
    path('services/', myviews.services, name= 'services'),
    path('services_detail/', myviews.services_detail, name= 'services_detail'),
    path('services_list/', myviews.services_list, name= 'services_list'),
    path('blog_list/', myviews.blog_list, name= 'blog_list'),
    path('blog_detail/', myviews.blog_detail, name= 'blog_detail'),
    path('blog_grid/', myviews.blog_grid, name= 'blog_grid'),

    path('contact/', myviews.contact, name= 'contact'),
    path('contact2/', myviews.contact2, name= 'contact2'),
    

    path('cart/', myviews.cart, name= 'cart'),

    path ('add-to-cart/', addtocart, name = 'addtocart' ),

    path('career/', myviews.career, name= 'career'),

    #path('checkout/', myviews.checkout, name= 'checkout'),
    path('price/', myviews.price, name= 'price'),

    path('faq/', myviews.faq, name= 'faq'),
    path('shop/', myviews.shop, name= 'shop'),
    path('shop_detail/', myviews.shop_detail, name= 'shop_detail'),
    path('shop_detail2/<str:slug>', myviews.shop_detail2, name= 'shop_detail2'),


    path('error/', myviews.error, name= 'error'),
    path('privacy_policy/', myviews.privacy_policy, name= 'privacy_policy'), 
    path('test/',  myviews.test, name ='test'),




]
