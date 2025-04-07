from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from genres.serializer import GenreSerializer
from actors.serializer import ActorSerializer



class MovieModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"
    
    def validate_release_date(self, value): # Validação de dados eu preciso colocar o nome validate_ com o nome do campo
        if value.year < 1990:
            raise serializers.ValidationError(' A data de lançamento não pode ser anterior a 1990.')#ValidationError valida o erro
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não pode ser maior que 200')
        return value

class MovieListDetailSerialzier(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)  #Reaproveita o serializer para trazer o objeto
    genre = GenreSerializer() #Agora o genero traz o Objeto e não o ID do genero
    
    rate = serializers.SerializerMethodField(read_only=True) #Variavel que segura a média das avaliações MethodField faz um serializer calcular
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']
          
    def  get_rate(self, obj): #serializers calculate eu preciso colocar o nome get_ com o nome da variavel
        rate = round(obj.reviews.aggregate(Avg('stars'))['stars__avg'], 1) #Agregate, adicione o campo Avg, que é a média
        #quero que só me traga o 'stars__avg'
        
        if rate:
            return rate

        return None
