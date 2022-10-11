from django.contrib import admin
from .models import Movie, Feedback
from django.db.models import Avg
from django.contrib.auth.models import User

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_average')
    search_fields = ['name']

    def show_average(self, obj):
        result = Feedback.objects.filter(movie=obj).aggregate(Avg("rating"))
        return result["rating__avg"]

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating', 'good', 'bad', 'full_name', 'date')
    list_filter = ['date', 'movie', 'user']
    search_fields = ['good', 'bad']
    def full_name(self, obj):
        first_name = obj.user.first_name
        last_name = obj.user.last_name
        if len(first_name) > 0 or len(last_name) > 0:
            return f"{obj.user.first_name} {obj.user.last_name}"
        else:
            return obj.user

  
admin.site.register(Movie, MovieAdmin)
admin.site.register(Feedback, FeedbackAdmin)


