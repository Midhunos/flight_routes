
from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_airport_route, name="add_airport_route"),
    path("nth-search/", views.nth_node_search, name="nth_node_search"),
    path("longest/", views.longest_node, name="longest_node"),
    path("shortest/", views.shortest_between_two, name="shortest_between"),
]