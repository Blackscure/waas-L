 
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apps/authentictaion/api/v1/', include('authentication.urls')),
    path('apps/entity-onboarding/api/v1/', include('entity_onboading.urls')),
]
