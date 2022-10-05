from django.contrib import admin
from .models import Movie, Feedback

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('elokuva', 'arvosana', 'plussat', 'miinukset', 'aika')
    list_filter = ['aika', 'elokuva']
    search_fields = ['plussat', 'miinukset']
   
admin.site.register(Movie, MovieAdmin)
admin.site.register(Feedback, FeedbackAdmin)


