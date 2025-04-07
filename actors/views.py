from rest_framework import generics
from actors.models import Actor
from actors.serializer import ActorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission




class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,) #Authentication de permissões, Verifica se o usuário está authenticado
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

