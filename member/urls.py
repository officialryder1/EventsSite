from django.urls import path
from .views import login_user, logout_user, register_user

urlpatterns = [
    path('signin', login_user, name='login'),
    path('signout', logout_user, name='logout'),
    path('signup', register_user, name='register')
]