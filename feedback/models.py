from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Feedback(models.Model):
    elokuva = models.ForeignKey(Movie, on_delete=models.CASCADE)
    arvosana_arvo = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    arvosana = models.IntegerField(choices = arvosana_arvo, default = 1)
    plussat = models.TextField(max_length=2000, blank=True)
    miinukset = models.TextField(max_length=2000, blank=True) 
    aika = models.DateTimeField(auto_now_add=True)
 
    
    def __str__(self):
        return f"{self.aika}"   
    