from django.core.checks import messages
from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse



# Create your views here.
def store(request):
    context={}
    return render(request,'store/store.html',context)

# def sports(request):
#     context={}
#     return render(request,'store/sports.html',context)

# def office_casual(request):
#     context={}
#     return render(request,'store/office_casual.html',context)

def cart(request):
    context={}
    return render(request,'store/cart.html',context)

def checkout(request):
    context={}
    return render(request,'store/checkout.html',context)

def ContactUs(request):
    if request.method=="POST":
        cont=Contact() #HERE I MADE OBJECT
        name=request.POST.get('name') #we have taken this name from input name contact html page 
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        query=request.POST.get('query')
         #here we have taken contact_.name=name the first name attribute is from models and the seocnd name attribute from this page means viwes(app)
        cont.name=name
        cont.email=email
        cont.contact=contact
        cont.query=query=query
        cont.save()
        messages.success(request,'Your message has been sent!')
    return render(request,'store/ContactUs.html')


def AboutUs(request):
    context={}
    return render(request,'store/AboutUs.html',context)

def Account(request):    
    return render(request,'store/Account.html')



