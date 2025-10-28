from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
# Create your views here.

def place_list (request):

  if request.method == 'POST':
    # Create a new place from the form
    # creating a form here
    form = NewPlaceForm(request.POST)
    #creating a model object from form.
    place = form.save()
    # validation against DB constraints
    if form.is_valid():
      # save place to db
      place.save()
      # reloads home page.
      return redirect('place_list')







  places = Place.objects.filter(visited=False).order_by('name')
  new_place_form = NewPlaceForm()
  return render (request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

def places_visited(request):
  visited = Place.objects.filter(visited=True)
  return render (request, 'travel_wishlist/visited.html', {'visited': visited})


def place_was_visited(request, place_pk):
  if request.method=='POST':
    # place = Place.objects.get(pk=place_pk)
    place = get_object_or_404(Place , pk=place_pk)
    place.visited = True
    place.save()
  return redirect ('place_list')
  # retrun redirect ('places_visited')



def about(request):
  author = 'Wolid'
  about = 'A websites to create a list of places to visit'
  return render(request, 'travel_wishlist/about.html', {'author': author,  'about': about})