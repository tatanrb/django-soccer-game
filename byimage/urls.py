from django.urls import path
from .views import game, find_out

urlpatterns = [
    path('', game),
    path('findout/', find_out)
]