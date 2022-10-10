from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Feedback(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating_grade = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    rating = models.IntegerField(choices = rating_grade, default = 1)
    good = models.TextField(max_length=2000, blank=True)
    bad = models.TextField(max_length=2000, blank=True) 
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    
    def __str__(self):
        return f"{self.date}"   
    