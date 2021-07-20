import json

from django.http     import JsonResponse
from django.views    import View

from movies.models import *

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        # actormovies = ActorMovie.objects.all()
        # movies = Movie.objects.all()
        results  = []
        for actor in actors:
            list = []
            for i in actor.movies.all():
                list.append(i.title)    
            # for i in actormovies.filter(actor_id = actor.id):
            #     list.append(Movie.objects.get(id=i.movie_id).title)
            results.append(
                {
                    "first_name"         : actor.first_name,
                    "last_name"          : actor.last_name,
                    "movie_list"         : list
                    }
            )
        return JsonResponse({'resutls':results}, status=200)

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        # actormovies = ActorMovie.objects.all()
        # actors = Actor.objects.all()
        results  = []
        for movie in movies:
            list = []
            for i in movie.actors.all():
                list.append(i.first_name)
            # for i in actormovies.filter(movie_id = movie.id):
            #     list.append(Actor.objects.get(id=i.actor_id).first_name)
            results.append(
                {
                    "title"                 : movie.title,
                    "running_time"          : movie.running_time,
                    "actor_list"            : list
                    }
            )
        return JsonResponse({'resutls':results}, status=200)