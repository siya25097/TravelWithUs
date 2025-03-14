# forms.py
from django import forms
from .models import BookNow

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookNow
        fields = ['email', 'name', 'booking_date', 'guests']

