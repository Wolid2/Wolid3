from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
# Create your models here.

class Place(models.Model):
  # linking each place to a specific user
  user = models.ForeignKey('auth.User',null=False, on_delete=models.CASCADE)
  #  name of the place
  name= models.CharField(max_length=200)
  # whether the place was visited or not the default is false
  visited= models.BooleanField(default=False)
  notes = models.TextField ( blank=True, null=True)
  date_visited = models.DateField (blank=True, null=True)
  photo = models.ImageField(upload_to='user_images/', blank=True, null=True )
# if the photo is updated, the old photo will be deleted from the file
  def save (self, *args, **kwargs):
    # check for an  existing place in the db
    old_place = Place.objects.filter (pk=self.pk).first()
    # if there is an old photo then it will delete it
    if old_place and old_place.photo:
      if old_place.photo != self.photo:
          self.delete_photo(old_place.photo)
    super().save(*args, **kwargs)

# deleting a specific photo from the storage
  def delete_photo(self, photo):
    if default_storage.exists(photo.name):
        default_storage.delete(photo.name)


# it will making sure that when a place is deleted, its photo is also deleted from the file
  def delete(self, *args, **kwargs):
    if self.photo:
        self.delete_photo(self.photo)
    super().delete(*args, **kwargs)

  def __str__(self):
    photo_str = self.photo.url if self.photo else "No Photo"
    notes_str = self.notes[100:] if self.notes else "No Notes"
    return f'{self.name} visited? {self.visited} on {self.date_visited}. Photo {photo_str}. Notes: {notes_str}'


