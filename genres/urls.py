from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre'),
    path('genres/<int:pk>/', views.GenreRetrieveUpadateDestroyView.as_view(), name='genre-detail-view'),
]



