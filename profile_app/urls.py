from django.urls import path, include
from profile_app.views import SignUpView, MyProfile

urlpatterns = [
    path('profile/<int:pk>', MyProfile.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
