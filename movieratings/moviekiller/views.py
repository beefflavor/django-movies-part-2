from django.shortcuts import render
from django.http import HttpResponse
from moviekiller.models import Movie
import datetime


def top_20_movies(requests):
    movies = Movie.objects.all()


    return HttpResponse("the top 20 rated movies")