from django.urls import path
from .views import register, user_login, welcome

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('welcome/<str:username>/', welcome, name='welcome'),

]
