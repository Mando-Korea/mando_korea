from django.urls import path
from . import views

urlpatterns = [
    path('', views.getemail, name='getemail'), #marketing
    path('index',views.index,name='index'),
    path('movie/<str:pk>/', views.movie, name='movie'),
    
]

# Source: https://www.youtube.com/watch?v=wiDewMGwuRs