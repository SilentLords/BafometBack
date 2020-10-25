from django.contrib import admin
from django.urls import path, include
from .views import PlacesView, AddToFavourite,AddToVisited, GetFavList,GetWatchList, GetOnePlace
urlpatterns = [
    path('/place/', PlacesView.as_view()),
    path('/add_to_visited/', AddToVisited.as_view()),
    path('/add_to_favourite/', AddToFavourite.as_view()),
    path('/get_favourite/', GetFavList.as_view()),
    path('/get_visited/', GetWatchList.as_view()),
    path('/get_one_place/', GetOnePlace.as_view())
]