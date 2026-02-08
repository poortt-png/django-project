from django.core.management.base import BaseCommand
from movies.models import Genre, Movie
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **options):
        # Create some genres
        genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance', 'Thriller', 'Animation']
        for genre_name in genres:
            genre, created = Genre.objects.get_or_create(name=genre_name)
            if created:
                self.stdout.write(f'Created genre: {genre_name}')

        # Create some sample movies
        sample_movies = [
            {'title': 'The Shawshank Redemption', 'director': 'Frank Darabont', 'year': 1994, 'genre': 'Drama'},
            {'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 1972, 'genre': 'Drama'},
            {'title': 'The Dark Knight', 'director': 'Christopher Nolan', 'year': 2008, 'genre': 'Action'},
            {'title': 'Pulp Fiction', 'director': 'Quentin Tarantino', 'year': 1994, 'genre': 'Crime'},
            {'title': 'Forrest Gump', 'director': 'Robert Zemeckis', 'year': 1994, 'genre': 'Drama'},
            {'title': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'genre': 'Sci-Fi'},
            {'title': 'The Matrix', 'director': 'Lana Wachowski, Lilly Wachowski', 'year': 1999, 'genre': 'Sci-Fi'},
            {'title': 'Goodfellas', 'director': 'Martin Scorsese', 'year': 1990, 'genre': 'Crime'},
            {'title': 'Parasite', 'director': 'Bong Joon-ho', 'year': 2019, 'genre': 'Thriller'},
            {'title': 'Spirited Away', 'director': 'Hayao Miyazaki', 'year': 2001, 'genre': 'Animation'},
        ]

        for movie_data in sample_movies:
            genre, _ = Genre.objects.get_or_create(name=movie_data['genre'])
            movie, created = Movie.objects.get_or_create(
                title=movie_data['title'],
                director=movie_data['director'],
                year=movie_data['year'],
                genre=genre
            )
            if created:
                self.stdout.write(f'Created movie: {movie_data["title"]}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with initial data')
        )