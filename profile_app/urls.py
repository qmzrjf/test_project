from django.urls import path, include
from profile_app.views import smoke

urlpatterns = [
    path('profile/', smoke, name='profile'),
]