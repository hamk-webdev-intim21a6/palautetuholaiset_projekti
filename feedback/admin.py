from django.contrib import admin
from .models import Movie, Feedback
from django.db.models import Avg

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_average')
    search_fields = ['name']

    def show_average(self, obj):
        result = Feedback.objects.filter(elokuva=obj).aggregate(Avg("arvosana"))
        return result["arvosana__avg"]

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('elokuva', 'arvosana', 'plussat', 'miinukset', 'aika')
    list_filter = ['aika', 'elokuva']
    search_fields = ['plussat', 'miinukset']

  
admin.site.register(Movie, MovieAdmin)
admin.site.register(Feedback, FeedbackAdmin)


