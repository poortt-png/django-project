from django.contrib import admin
from .models import Genre, Movie, Review


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'year', 'genre', 'created_at', 'has_poster']
    list_filter = ['year', 'genre', 'created_at']
    search_fields = ['title', 'director']
    date_hierarchy = 'created_at'

    def has_poster(self, obj):
        return bool(obj.poster)
    has_poster.short_description = 'Has Poster'
    has_poster.boolean = True


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'movie']
    search_fields = ['user__username', 'movie__title', 'comment']
    date_hierarchy = 'created_at'