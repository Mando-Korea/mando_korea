#i think urls is what you write first, then views
from django.urls import path, include
from . import views
from .views import email_view
from django.contrib import admin

urlpatterns = [
    path('', views.getemail, name='getemail'), #marketing
    path('index',views.index,name='index'),
    path('movie/<str:pk>/', views.movie, name='movie'),
    path('redirect/', views.after_email, name='after_email' ),
    path('', email_view, name='email_view'),
    path('', include('paypal.standard.ipn.urls'))
]

# Source: https://www.youtube.com/watch?v=wiDewMGwuRs

