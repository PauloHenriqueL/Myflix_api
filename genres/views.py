from genres.models import Genre
from rest_framework import generics
from genres.serializer import GenreSerializer

#VIEWS COM RESETFRAMEWORK

class GenreCreateListView(generics.ListCreateAPIView): #lista e cria
    queryset = Genre.objects.all() #Lista todos os objetos do banco de dados
    serializer_class = GenreSerializer #Serializa
        
        
class GenreRetrieveUpadateDestroyView(generics.RetrieveUpdateDestroyAPIView): #Deleta, update, detalha
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer       
