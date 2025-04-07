from rest_framework import generics, views, response, status
from django.db.models import Count, Avg
from reviews.models import Review
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieListDetailSerialzier
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerialzier
        return MovieModelSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerialzier
        return MovieModelSerializer
    
class MovieStatsView(views.APIView):  #Crio minha própria Api para trazer as estatíticas
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)  #permissões
    queryset = Movie.objects.all()  #Falo qual o model
    
    def get(self,request):  #Se for get
        total_movies = self.queryset.count()  #O total de movies
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))  #Values traz uma coluna específica. Quantos registro há de cada genero
        total_reviews = Review.objects.count()  #O total de reviews
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']  #A média de estrelas
        
        return response.Response(data={#  Responda isso para get
            "total_movies":total_movies,
            "movies_by_genre":movies_by_genre,
            "total_reviews" :total_reviews,   
            "average_stars": round(average_stars, 1) if average_stars else 0,
        }, status=status.HTTP_200_OK)  #Arredendo a média de estrelas, se não tiver estrelas você dar 0
