from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from tripz.models import Blog, Hotel



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = auth.authenticate(username=username, password=password)
        
     
        if user is not None:
            auth.login(request,user)
            return redirect('/')
     
        else: 
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
       return render(request,'login.html')
        


# Create your views here
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']


        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                 messages.info(request, 'email taken')
                 return redirect('register')

            else:    
                user= User.objects.create_user(username=username, password= password1, email= email, first_name= first_name, last_name=last_name )
                user.save();
                return redirect('login')
            
        else:
            messages.info(request,'passwords do not match') 
            return redirect('register')


    else:
        return render(request,'register.html')
    



def logout(request):
    auth.logout(request)
    return redirect('/')



def searchhotel(request):
    if request.method == 'GET':
        is_private = request.POST.get('is_private', False)
        state=request.GET['state']
        val= Hotel.objects.filter(state__icontains = state)

        return render(request,'hotel.html',{'val': val})


def hotdetail(request,price):

    val= Hotel.objects.filter(price=price).first()
    return render(request,'hotdetail.html',{'val': val})
    # return HttpResponse("hello world")

def blog(request):
    b= Blog.objects.all()
    return render(request,'blog.html',{'b':b} )


def comments(request):
    # return HttpResponse("hello")

    if request.method == 'POST':
            name = request.POST['name']
            
            comment = request.POST['comment']  
           


    b= Blog.objects.create(name=name, review=comment)
    b.save();
    b= Blog.objects.all()
    return render(request,'comments.html',{'b':b} )


    