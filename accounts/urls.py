from django.urls import path
from . import views 

urlpatterns = [ 
               path("register", views.register, name="register"),
               path("login", views.login, name="login"),
               path("logout", views.logout, name="logout"),

               path('searchhotel',views.searchhotel,name='searchhotel'),
               path('hotdetail/<str:price>',views.hotdetail,name='hotdetail'),
               path("blog", views.blog, name="blog"),
               path("comments", views.comments, name="comments"),
               
               ]

