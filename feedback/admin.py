from django.contrib import admin
from .models import Movie, Feedback

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating', 'good', 'bad', 'date')
    list_filter = ['date', 'movie']
    search_fields = ['good', 'bad']
   
admin.site.register(Movie, MovieAdmin)
admin.site.register(Feedback, FeedbackAdmin)


