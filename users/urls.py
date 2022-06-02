from django import views
from django.urls import path
from .views import login_api, get_user_id, register_api
from knox import views as knox_views

urlpatterns = [
    path('login/', login_api, name='login_api'),
    path('user/', get_user_id, name='user'),
    path('register/', register_api, name='register'),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),

]
