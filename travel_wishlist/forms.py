from django import forms
from django.forms import FileInput, DateInput
from .models import Place

# this form is used to add a new place
class NewPlaceForm(forms.ModelForm):
    class Meta:
        # linking the form to the Place model
        model = Place
        fields = ('name', 'visited')

class DateInput(forms.DateInput):
    input_type = 'date'





# this form is used to review a trip when a place they have visited
class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo')
        widgets = {
            'date_visited': DateInput(),
            'photo': FileInput(),
        }