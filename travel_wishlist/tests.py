from django.test import TestCase
from django.urls import reverse
from .models import Place
# Create your tests here.
# testing the wishlist page when the db is empty
class PlaceTests(TestCase):

  def test_home_page_shows_empty_list_message_for_empty_database(self):
    # it will get the home page url.
    home_page_url = reverse('place_list')
    # iut will get a response from the home page
    response = self.client.get(home_page_url)
    # it will check if the correct template is used
    self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
    # it will check that the message for an empty list show up
    self.assertContains(response, 'You have no places in your wishlist')



class TestWishList(TestCase):
# use test data from fixture file
  fixtures = ['test_places']

  def test_wishlist_contains_not_visited_places(self):
    # it will get the wishlist page
    response = self.client.get(reverse('place_list'))
    # it will check if the correct template is used
    self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
    # it will check if the unvisited places are shown
    self.assertContains(response, 'Tokyo')
    # it will check if the unvisited places are shown
    self.assertContains(response, 'New York')
    # it will check if the visited places are not shown
    self.assertNotContains(response, 'San Francisco')
    self.assertNotContains(response, 'Moab')

class TestVisitedPages(TestCase):
# testing the visited page when the db is empty
  def test_visited_page_shows_empty_list_message_for_empty_database(self):
    # it will get the visited page
    response = self.client.get(reverse('places_visited'))
    # it will check the correct template
    self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
    # it will check the empty message show up
    self.assertContains(response, 'You have not visited any places yet')

  
class VisitedList(TestCase):
# use test data from fixture file
  fixtures = ['test_places']

  def test_visited_list_shows_visited_places(self):
    # it will get the visited page
    response = self.client.get(reverse('places_visited'))
    # it will check the correct template
    self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
    # it will check if the visited places are shown
    self.assertContains(response, 'San Francisco')
    self.assertContains(response, 'Moab')
    # it will check if the unvisited places are not shown
    self.assertNotContains(response, 'Tokyo')
    self.assertNotContains(response, 'New York')


class TestAddNewPlace(TestCase):

  def test_add_unvisited_place(self):
    # it will get the place add url
    add_place_url = reverse('place_list')
    # it will create a data for new visit place
    new_place_data = {'name': 'Tokyo', 'visited': False}
    # it will send the data using a POST
    response = self.client.post(add_place_url, new_place_data, follow=True)
    # it will check the correct template
    self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
    # it will get the list of places from the page.
    response_places = response.context['places']
    # it will check that there is one place now in the list
    self.assertEqual(1, len(response_places))

    # it will get the place from page
    tokyo_from_response = response_places[0]
    # it will get the same place from the database
    tokyo_from_database = Place.objects.get(name='Tokyo', visited=False)
    self.assertEqual(tokyo_from_database, tokyo_from_response)


class TestVisitedPlace(TestCase):
# use test data from fixture file
  fixtures = ['test_places']

  def test_visit_place(self):
    # it will get the visit place with ID.
    visit_place_url = reverse('place_was_visited', args=(2,))
    response = self.client.post(visit_place_url, follow=True)
  # it will check the correct template
    self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
  # it will check that 'New York' is no longer on the wishlist page
    self.assertNotContains(response, 'New York')  
  # it will check that 'Tokyo' is still on the wishlist page
    self.assertContains(response, 'Tokyo')
  # it will check that 'New York' is now on the visited page
    new_york = Place.objects.get(pk=2)
    self.assertTrue(new_york.visited)


  def test__non_existent_place(self): 
    # it will try to visit a place that does not exist
    visit_non_existent_place_url = reverse('place_was_visited', args=(120345,))
    # it will send a post request to the url
    response = self.client.post(visit_non_existent_place_url) 
    

