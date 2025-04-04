from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie (models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    genre = models.ForeignKey( #Serve para ligar a o outro model
        Genre, #model genre
        on_delete=models.PROTECT, #Protege ela de ser deletada
        related_name='movies' #Dar um nome para essa ligação
    ) 
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')#Muitos para muitos, deixou várias ligações a um mesmo filme e muitas ligações a o mesmo ator
    resume = models.TextField(null=True, blank=True) #Texto muito grande
    
    def __str__(self):
        return self.title