from django.urls import path

from authentication.views import AutheticationAPIView


urlpatterns = [
    path('auth/', AutheticationAPIView.as_view(), name='login-api'),
]