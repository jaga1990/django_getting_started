from django.urls import path
from .views import detail, room_detail, rooms_list 

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('<int:id>', room_detail, name='room_detail'),
    path('roomslist', rooms_list, name='rooms_list'),
]