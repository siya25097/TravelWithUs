from django.urls import path
from . import views
from signup.views import signaction
from login.views import loginaction
from .views import book_now
urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('packages/', views.packages, name='packages'),
    path('contact/', views.contact, name='contact'),
    path('signup/',signaction,name='signup'),
    path('login/', loginaction,name='login'),
    path('book-now/', views.book_now, name='book_now'), 
]
