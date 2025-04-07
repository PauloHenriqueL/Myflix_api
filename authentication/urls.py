from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('authentication/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#Gera um novo token que dura 5 min. Refresh token dura 24 horas
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),#Verifica se o token ainda esta valido
]