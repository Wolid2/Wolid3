from django.urls import path
from . import views

# it will list of the url paths for the travel_wishlist app
urlpatterns = [
  # the home page url - shows the place list
    path('' , views.place_list, name='place_list'),
    # the visited places page url.
    path('visited', views.places_visited, name='places_visited'),
    # the place was visited url
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name= 'place_was_visited'),
    # it will show the page about the website
    path('about',  views.about, name= 'about'),
    path('place/<int:place_pk>', views.place_details, name='place_details'),
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place'),
]




