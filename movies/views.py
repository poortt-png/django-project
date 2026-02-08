from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.views import LoginView
from .models import Movie, Genre, Review
from .forms import ReviewForm, UserRegistrationForm


def movie_list(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    
    # Filtering
    genre_id = request.GET.get('genre')
    year = request.GET.get('year')
    
    if genre_id:
        movies = movies.filter(genre_id=genre_id)
    
    if year:
        movies = movies.filter(year=year)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        movies = movies.filter(Q(title__icontains=query) | Q(director__icontains=query))
    
    # Get unique years for filter dropdown
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('-year')
    
    context = {
        'movies': movies,
        'genres': genres,
        'selected_genre': genre_id,
        'selected_year': year,
        'years': years,
        'query': query,
    }
    return render(request, 'movies/movie_list.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You need to log in to leave a review.')
            return redirect('login')
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('movie_detail', pk=pk)
    else:
        form = ReviewForm()
    
    context = {
        'movie': movie,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'movies/movie_detail.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('login')  # Redirect to login page instead of auto-login
            except Exception as e:
                messages.error(request, f'Registration failed: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})




@login_required
def add_movie(request):
    # This would be implemented if we want users to add movies
    # For now, only admin can add movies through admin panel
    pass