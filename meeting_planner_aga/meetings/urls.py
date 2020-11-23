from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('room/<int:id>', views.room_detail, name='room_detail'),
    path('roomslist', views.rooms_list, name='rooms_list'),
    path('newForm', views.new, name="new")
]