from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# anna palaute
# aihe (web-kodaamisen perusteet (5 op))
# arvosana 1-100
# hyvää
# huonoa
# automaattisesti luotu aikaleima

class Movie(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    good = models.TextField(max_length=2000, blank=True)
    bad = models.TextField(max_length=2000, blank=True) 
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.date}"
    
    