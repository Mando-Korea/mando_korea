from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movie, MovieList
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect         #email cookie 
import re

# Create your views here.
def index(request):
    # movies = Movie.objects.all()
    # featured_movie = movies[len(movies)-1] 
    # context = {
    #     'movies': movies,
    #     'featured_movie': featured_movie,
    # }
    return render(request, 'index.html')  #, context deleted from inside render()

def movie(request, pk):
    movie_uuid = pk
    movie_details = Movie.objects.get(uu_id=movie_uuid)

    context = {
        'movie_details': movie_details
    }
    return render(request, 'movie.html', context)

def getemail(request):
    return render(request, 'getemail.html')

def set_user_email_cookie(request):  #setting cookie onn serverside
    response = HttpResponseRedirect('getemail.html')
    # Set the cookie with the user's email after they've logged in or registered
    response.set_cookie('userEmail', 'user@example.com', max_age=2592000)  # Expires in 30 days
    return response