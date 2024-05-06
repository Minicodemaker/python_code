from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Blog, Destination
from . models import Hotel
from django.contrib.auth.models import User,auth




# Display all destinations on home page(fetch all rows)
def index(request):

    dests= Destination.objects.all()
    return render(request,"index.html", {'dests': dests} )


# search a destiation
def search(request):


    if request.method == 'GET':
        name = request.GET['City']
            
        dests = Destination.objects.filter(name__icontains=name)
        
        return render(request,'search.html',{'dests': dests})
    


# to show destinations with offer only not others 

def bestprice(request):
     
    
    if request.user.is_authenticated:
            
        dests = Destination.objects.filter(offer = True)
        
        return render(request,'offer.html',{'dests': dests})  

    else:
       
       return redirect('login')  


# 1.  city function has been used to fetch all the data of a particular city dynamically
# 2. price has been used as a slug here(we can use any other attribute from the model destination)
# 3.  slug is used to filter out the rows from the database.


def city(request,price):

    if request.user.is_authenticated:
    
        dests= Destination.objects.filter(price=price).first()
        return render(request,"description.html", {'dests':dests})
    else:
        return redirect('login')
    


    
# contact and aboutUs is same
def contact(request):
    return render(request,"contact.html")




# ----------------------- model=hotel------------------#

def bookhotel(request):
    h= Hotel.objects.all()
    return render(request,"bookhotel.html",{'h':h})


#-----------------------model - Blog --------------#
def testimonials(request):

    b= Blog.objects.all()
    return render(request,"index.html", {'b': b} )





    

