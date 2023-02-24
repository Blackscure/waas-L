from django.urls import path

from entity_onboading.views import EntityOnboardingAPIView



urlpatterns = [
    path('entity-onboarding/', EntityOnboardingAPIView.as_view(), name='waas-api'),
]