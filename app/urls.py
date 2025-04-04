
from django.contrib import admin
from django.urls import path
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from genres.views import GenreCreateListView, GenreRetrieveUpadateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('genres/', GenreCreateListView.as_view(), name='genre'),
    path('genres/<int:pk>/', GenreRetrieveUpadateDestroyView.as_view(), name='genre-detail-view'),

    path('movies/', MovieCreateListView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-Retrieve-Update-Destroy'),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-Retrieve-Update-Destroy'),
 
    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-Retrieve-Update-Destroy')
]