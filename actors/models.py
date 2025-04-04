from django.db import models


NATIONALITY_CHOICES = ( #Varivel constante tem que ser em maisculo
    ("USA", "Estados Unidos"), #Você dar o valor em Tuplas com o valor que vai ficar no banco de dados e o que vai aparecer
    ("BR", "Brasil"),    
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationaly = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES, #Você obriga a ser uma validação de dados
        blank = True,
        null = True,
    )
    
    def __str__(self):
        return self.name