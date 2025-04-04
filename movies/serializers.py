from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg



class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True) #Variavel que segura a média das avaliações MethodField faz um serializer calcular
    
    class Meta:
        model = Movie
        fields = "__all__"
        
    def  get_rate(self, obj): #serializers calculate eu preciso colocar o nome get_ com o nome da variavel
        rate = round(obj.reviews.aggregate(Avg('stars'))['stars__avg'], 1) #Agregate, adicione o campo Avg, que é a média
        #quero que só me traga o 'stars__avg'
        
        if rate:
            return rate

        return None
        
        #reviews = obj.reviews.all() # chamo a relação entre os models reviews e models movies
        
        
        #reviews = obj.reviews.filter( 
        #     stars__Ite=3) faço o filtro até 3 estrelas
        
        #if reviews: #Se ele tem pelo menos um reviews faça isso
        #    sum_reviews = 0
        #    for review in reviews:
        #        sum_reviews += review.stars #para cada obj em reviews soma esse valor, para que eu pegue o total

        #    reviews_count = reviews.count() #para que eu pegue a quantidade de objetos
            
        #    return round(sum_reviews / reviews_count, 1)
    
        #return None
            
        
        
    def validate_release_date(self, value): # Validação de dados eu preciso colocar o nome validate_ com o nome do campo
        if value.year < 1990:
            raise serializers.ValidationError(' A data de lançamento não pode ser anterior a 1990.')#ValidationError valida o erro
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não pode ser maior que 200')
        return value

    
