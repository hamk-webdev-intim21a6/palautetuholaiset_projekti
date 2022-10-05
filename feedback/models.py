from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    elokuva = models.ForeignKey(Movie, on_delete=models.CASCADE)
    arvosana = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    plussat = models.TextField(max_length=2000, blank=True)
    miinukset = models.TextField(max_length=2000, blank=True) 
    aika = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.aika}"
    
    