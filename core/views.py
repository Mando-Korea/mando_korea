#Views is what u write seconnd i think
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from core.models import Movie, MovieList
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect         #email cookie
from django import forms 
from .forms import EmailForm
from .models import EmailModel
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

def after_email(request):  #behavior im trying to make happen after they input email
    # if request.method == 'POST':
        # Perform some action
        # return redirect('target_view')
    return render('index.html')

def email_view(request):     #accepts emails to store at postgresql
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            #save the email to the database
            EmailModel.objects.create(email=email)
            #Redirect to a new URL
            return redirect('index') #your URL goes here
        else:
            form = EmailForm()

        return render(request, '', {'form': form})
        

