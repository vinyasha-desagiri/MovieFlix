from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Movie


def home(request):
    movies = Movie.objects.all()

    return render(request, 'movies/home.html', {
        'movies': movies
    })


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    return render(request, 'movies/movie_detail.html', {
        'movie': movie
    })


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'Account created successfully.')

        return redirect('login')

    return render(request, 'movies/register.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'movies/login.html')


def user_logout(request):

    logout(request)

    return redirect('home')