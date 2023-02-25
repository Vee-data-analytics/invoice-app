from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
 CreateProfileView,
 ProfileUpdateView,
 ProfileDetailView,
 logout_view,
 signup_view,
)

app_name = 'profiles'

urlpatterns = [
    path('logout/', logout_view, name='account_logout'),
    path('signup/', signup_view, name='account_signup'),
    path('profilecreate/', login_required(CreateProfileView.as_view()), name='profile_create' ),
    path('profile/<str:username>',login_required(ProfileDetailView.as_view()), name='profile_detail'),
    path('profileupdate/<str:username>/',login_required(ProfileUpdateView.as_view()), name='profile_update')
]