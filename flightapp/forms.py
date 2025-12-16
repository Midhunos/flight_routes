from django import forms
from .models import AirportRoute

class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = ['airport_code', 'parent', 'position', 'duration']
