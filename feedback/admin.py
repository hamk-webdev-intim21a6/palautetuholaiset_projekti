from django.contrib import admin
from .models import Movie, Feedback
from django.db.models import Avg

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_average')
    search_fields = ['name']

    def show_average(self, obj):
        result = Feedback.objects.filter(movie=obj).aggregate(Avg("rating"))
        return result["rating__avg"]

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating', 'user', 'good', 'bad', 'date')
    list_filter = ['date', 'movie']
    search_fields = ['good', 'bad']

  
admin.site.register(Movie, MovieAdmin)
admin.site.register(Feedback, FeedbackAdmin)
