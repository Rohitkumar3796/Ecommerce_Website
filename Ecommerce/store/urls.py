from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    # path('office_casual/',views.office_casual,name='office_casual'),
    # path('sports/',views.sports,name='sports'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('ContactUs/',views.ContactUs,name='ContactUs'),
    path('AboutUs/',views.AboutUs,name='AboutUs'),
    path('Account/',views.Account,name='Account'),
    
    

]