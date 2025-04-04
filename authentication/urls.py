from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

#Cria um token para verificar a pessoa. Precisa instalar 'djangorestframework-simplejwt' e criar o app Authentication
#Em seetings precisa colocar que rest_framework_simplejwt em Instaled app E pasta Authentication
#Ainda em ssetings você precisa falar que ele vai usar a class simplewjwt.
    #REST_FRAMEWORK = {
    #    'DEFAULT_AUTHENTICATION_CLASSES': (
    #        'rest_framework_simplejwt.authentication.JWTAuthentication',
    #    ),
    #}
#Em app.urls precisa colocar a nova urls




urlpatterns = [
    path('authentication/token/',TokenObtainPairView.as_view(), name='token_obtain_pair')
    
]