from django.urls import path
from .views import *

urlpatterns = [
    # path('', accueil, name="accueil"),
    path('', home, name="home"),
    path('<str:room>/', room, name="romm"),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
    path('getRooms/<str:util>/', getRooms, name='getRooms'),
    path('createRoom/<str:u1>/<str:u2>', createRoom, name='createRoom'),
]