from django.urls import path
from . import views 

urlpatterns = [ 
               path('', views.index, name='index'),
               path('index', views.index, name='index'),
               path('contact', views.contact, name='contact'),
               
               path('search',views.search,name='search'),
               #here price has been used as a slug to fetch the values from the database
               path('city/<str:price>',views.city,name='city'),
               path('bestprice',views.bestprice,name='bestprice'),

               path('bookhotel',views.bookhotel,name='bookhotel'),
               path('testimonials',views.testimonials,name='testimonials'),
               
        
               
               ]

