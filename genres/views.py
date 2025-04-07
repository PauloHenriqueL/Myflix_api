from genres.models import Genre
from rest_framework import generics
from genres.serializer import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
#VIEWS COM RESETFRAMEWORK

class GenreCreateListView(generics.ListCreateAPIView): #lista e cria
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all() #Lista todos os objetos do banco de dados
    serializer_class = GenreSerializer #Serializa
        
        
class GenreRetrieveUpadateDestroyView(generics.RetrieveUpdateDestroyAPIView): #Deleta, update, detalha
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer       
