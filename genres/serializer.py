from rest_framework import serializers
from genres.models import Genre

class GenreSerializer(serializers.ModelSerializer): #ModelSerializer é como o modelform é para o form
    
    class Meta:
        model = Genre
        fields = '__all__'